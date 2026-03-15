from flask import *

app = Flask(__name__)
app.secret_key = "backrooms_secret"

FLAGS = {
    1: {"flag": "BCKRM{bon_début}", "points": 100, "redirect": "/level2"},
    2: {"flag": "06:10", "points": 100, "redirect": "/level2"},
    3: {"flag": "6515", "points": 300, "redirect": "/level4"},
    }

@app.route('/')
def accueil():
    return redirect('/level0')

# ── Pages des niveaux ────────────────────────────────────────────────────
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

@app.route('/level2')
def level2():
    return send_from_directory('level2', 'level2.html')

@app.route('/level2.1')
def level2_1():
    return send_from_directory('level2', 'level2.1.html')

@app.route('/level3')
def level3():
    return send_from_directory('level3', 'level3.html')

# ── Fichiers statiques de chaque niveau (CSS, etc.) ──────────────────────
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

# ── Images et sons (dossiers partagés) ───────────────────────────────────
@app.route('/images/<path:fichier>')
def images(fichier):
    return send_from_directory('images', fichier)

@app.route('/sons/<path:fichier>')
def sons(fichier):
    return send_from_directory('sons', fichier)

# ── Vérification des flags ───────────────────────────────────────────────
@app.route('/verifier/<int:niveau>', methods=['POST'])
def verifier(niveau):
    data = request.get_json()
    flag_soumis = data['flag'].strip()

    if niveau not in FLAGS:
        return jsonify({"succes": False, "message": "Niveau inconnu"})

    if flag_soumis == FLAGS[niveau]["flag"]:
        return jsonify({"succes": True, "redirect": FLAGS[niveau]["redirect"]})
    else:
        return jsonify({"succes": False, "message": "❌ Mauvais flag."})

if __name__ == '__main__':
    app.run(debug=True)