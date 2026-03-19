from flask import *
from database import init_db, ajouter_joueur, valider_niveau, get_niveaux_valides, get_leaderboard

app = Flask(__name__)
app.secret_key = "backrooms_secret"

init_db()

import os
app.secret_key = os.urandom(24)

# Ordre obligatoire des niveaux (anticheat)
ORDRE_NIVEAUX = {
    '/level1':   1,
    '/level1.1': 1,
    '/level1.2': 1,
    '/level1.3': 1,
    '/level2':   4,
    '/level2.1': 4,
    '/level3':   5,
    '/level3.5': 5,
    '/level4':   5,
    '/level4.1': 5,
    '/level4.2': 5,
    '/level4.3': 5,
    '/level5':   44,
}

def niveau_accessible(pseudo, route):
    if pseudo.lower() == "admin":
        return True
    for chemin, flag_requis in ORDRE_NIVEAUX.items():
        if route.startswith(chemin):
            valides = get_niveaux_valides(pseudo)
            if flag_requis not in valides:
                return False
    return True

FLAGS = {
    # Level 0
    1:  {"flag": "391",     "points": 100, "redirect": "/level1"},
    # Level 1
    2:  {"flag": "06:10",   "points": 50,  "redirect": "/level2"},
    3:  {"flag": "5130003", "points": 25,  "redirect": "/level2"},
    4:  {"flag": "007365",  "points": 25,  "redirect": "/level2"},
    # Level 3
    5:  {"flag": "6515",    "points": 150, "redirect": "/level4"},
    # Level 4 sous-énigmes
    41: {"flag": "4301",    "points": 100, "redirect": "/level4"},
    42: {"flag": "19",      "points": 100, "redirect": "/level4"},
    43: {"flag": "1974",    "points": 100, "redirect": "/level4"},
    # Level 4 code final
    44: {"flag": "430119",  "points": 300, "redirect": "/level5"},
}

# === PAGE PSEUDO ===
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pseudo = request.form.get('pseudo', '').strip()
        if not pseudo or len(pseudo) > 20:
            return render_template_string(LOGIN_HTML, erreur="Pseudo invalide.")
        ajouter_joueur(pseudo)
        session['pseudo'] = pseudo
        return redirect('/')
    return render_template_string(LOGIN_HTML, erreur=None)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# === MIDDLEWARE — vérifie pseudo + anticheat ===
@app.before_request
def verifier_acces():
    routes_libres = ['/login', '/logout', '/static', '/images', '/sons', '/level0']

    if request.path == '/':
        if 'pseudo' not in session:
            return redirect('/login')
        return

    if any(request.path.startswith(r) for r in routes_libres):
        return

    if 'pseudo' not in session:
        return redirect('/login')

    pseudo = session['pseudo']
    if not niveau_accessible(pseudo, request.path):
        return redirect('/')

@app.route('/')
def accueil():
    return redirect('/level0')

@app.route('/verifier/<int:niveau>', methods=['POST'])
def verifier(niveau):
    pseudo = session.get('pseudo')
    if not pseudo:
        return jsonify({"succes": False, "message": "Non connecté."})

    data = request.get_json()
    flag_soumis = data['flag'].strip()

    if niveau not in FLAGS:
        return jsonify({"succes": False, "message": "Niveau inconnu"})

    if flag_soumis == FLAGS[niveau]["flag"]:
        valider_niveau(pseudo, niveau, FLAGS[niveau]["points"])
        return jsonify({"succes": True, "redirect": FLAGS[niveau]["redirect"]})
    else:
        return jsonify({"succes": False, "message": "❌ Mauvais flag."})

@app.route('/leaderboard')
def leaderboard():
    scores = get_leaderboard()
    return render_template_string(LEADERBOARD_HTML, scores=scores)

# === TEMPLATES INLINE ===
LOGIN_HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Backrooms — Identification</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            background: #080807;
            font-family: 'Courier New', monospace;
            display: flex; align-items: center; justify-content: center;
            height: 100vh; color: #a89e72;
        }
        .box {
            border-left: 2px solid #c8a84a;
            padding: 2.5rem 2rem;
            background: rgba(0,0,0,0.82);
            max-width: 420px; width: 90%;
        }
        .titre { font-size: 0.6rem; letter-spacing: 0.4rem; color: #c8a84a; margin-bottom: 2rem; }
        input {
            width: 100%; background: transparent; border: 1px solid #2a2a1a;
            color: #e8dc9e; font-family: 'Courier New', monospace;
            font-size: 1rem; padding: 0.8rem 1rem; margin-bottom: 1rem; outline: none;
        }
        input:focus { border-color: rgba(232,220,158,0.3); }
        button {
            background: transparent; border: 1px solid #3a3a2a; color: #e8dc9e;
            font-family: 'Courier New', monospace; font-size: 0.78rem;
            padding: 0.8rem 2rem; cursor: pointer; text-transform: uppercase;
            letter-spacing: 0.2rem; transition: all 0.4s;
        }
        button:hover { border-color: #c8a84a; color: #c8a84a; }
        .erreur { color: #cc5555; font-size: 0.75rem; margin-top: 1rem; }
    </style>
</head>
<body>
    <div class="box">
        <div class="titre">BACKROOMS // IDENTIFICATION</div>
        <p style="margin-bottom:1.5rem; font-size:0.85rem;">Entrez votre pseudo pour commencer ou reprendre votre progression.</p>
        <form method="POST">
            <input type="text" name="pseudo" placeholder="PSEUDO" maxlength="20" autofocus>
            <button type="submit">ENTRER</button>
        </form>
        {% if erreur %}<p class="erreur">{{ erreur }}</p>{% endif %}
    </div>
</body>
</html>
"""

LEADERBOARD_HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Backrooms — Leaderboard</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#080807; font-family:'Courier New',monospace; color:#a89e72; padding:3rem 2rem; }
        h1 { font-size:0.6rem; letter-spacing:0.4rem; color:#c8a84a; margin-bottom:2rem; }
        table { width:100%; max-width:500px; border-collapse:collapse; }
        td, th { padding:0.6rem 1rem; font-size:0.85rem; border-bottom:1px solid #1a1a0e; }
        th { color:#c8a84a; font-size:0.6rem; letter-spacing:0.2rem; }
        .rang { color:#3a3a2a; width:40px; }
        a { color:#3a3a2a; font-size:0.7rem; text-decoration:none; display:block; margin-top:2rem; }
        a:hover { color:#c8a84a; }
    </style>
</head>
<body>
    <h1>BACKROOMS // LEADERBOARD</h1>
    <table>
        <tr><th>#</th><th>PSEUDO</th><th>POINTS</th></tr>
        {% for i, (pseudo, points) in enumerate(scores) %}
        <tr>
            <td class="rang">{{ i+1 }}</td>
            <td>{{ pseudo }}</td>
            <td>{{ points }}</td>
        </tr>
        {% endfor %}
    </table>
    <a href="/">← RETOUR</a>
</body>
</html>
"""

# === ROUTES ===
@app.route('/level0')
def level0():
    return send_from_directory('level0', 'level0.html')

@app.route('/level0.1')
def level0_1_direct():
    return send_from_directory('level0', 'level0.1.html')

@app.route('/level1')
def level1():
    return send_from_directory('level1', 'level1.html')

@app.route('/level1.1')
def level1_1():
    return send_from_directory('level1', 'level1.1.html')

@app.route('/level1.2')
def level1_2():
    return send_from_directory('level1', 'level1.2.html')

@app.route('/level1.3')
def level1_3():
    return send_from_directory('level1', 'level1.3.html')

@app.route('/level2')
def level2():
    return send_from_directory('level2', 'level2.html')

@app.route('/level2.1')
def level2_1():
    return send_from_directory('level2', 'level2.1.html')

@app.route('/level3')
def level3():
    return send_from_directory('level3', 'level3.html')

@app.route('/level4')
def level4():
    return send_from_directory('level4', 'level4.html')

@app.route('/level4.1')
def level4_1():
    return send_from_directory('level4', 'level4_1.html')

@app.route('/level4.2')
def level4_2():
    return send_from_directory('level4', 'level4_2.html')

@app.route('/level4.3')
def level4_3():
    return send_from_directory('level4', 'level4_3.html')

@app.route('/level0/<path:fichier>')
def level0_static(fichier):
    return send_from_directory('level0', fichier)

@app.route('/level1/<path:fichier>')
def level1_static(fichier):
    return send_from_directory('level1', fichier)

@app.route('/level2/<path:fichier>')
def level2_static(fichier):
    return send_from_directory('level2', fichier)

@app.route('/level3/<path:fichier>')
def level3_static(fichier):
    return send_from_directory('level3', fichier)

@app.route('/level4/<path:fichier>')
def level4_static(fichier):
    return send_from_directory('level4', fichier)

@app.route('/images/<path:fichier>')
def images(fichier):
    return send_from_directory('images', fichier)

@app.route('/sons/<path:fichier>')
def sons(fichier):
    return send_from_directory('sons', fichier)

if __name__ == '__main__':
    app.run(debug=True)
