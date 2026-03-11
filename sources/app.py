from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
app.secret_key = "backrooms_secret"

FLAGS = {
    1: {"flag": "BCKRM{bon_début}", "points": 100, "redirect": "/level2"},
}

# ── Pages des niveaux ────────────────────────────────────────────────────
@app.route('/level0')
def level0():
    return send_from_directory('level0', 'level0.html')

@app.route('/level1')
def level1():
    return send_from_directory('level1', 'level1.html')

@app.route('/level2')
def level2():
    return send_from_directory('level2', 'level2.html')

# ... tu ajouteras level3, 4, 5 au fur et à mesure

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