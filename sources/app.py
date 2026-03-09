from flask import Flask, render_template, request, redirect, send_from_directory, make_response
import os

app = Flask(__name__)

# --- ROUTES DU LEVEL 0 ---

@app.route('/')
def level0():
    return render_template('level0.html')

@app.route('/video_proxy')
def video_proxy():
    # Envoie la vidéo avec l'indice de date dans le header
    response = make_response(send_from_directory('static', 'Backroom_intro.mp4'))
    response.headers['X-Temporal-Data'] = "JULY-2024"
    return response

@app.route('/level0exploration')
def level0exploration():
    return render_template('level0exploration.html')

@app.route('/static/style0.css')
def hashed_css():
    # On définit le chemin absolu vers le fichier pour éviter l'erreur
    base_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(base_dir, 'static', 'style0.css')
    
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # On ajoute l'indice secret
        secret = "\n\n/*?????????? 30b030372733362e352257 ??????????*/"
        response = make_response(content + secret)
        response.headers['Content-Type'] = 'text/css'
        return response
    except FileNotFoundError:
        # Si vraiment il ne trouve rien, il renvoie une erreur plus propre
        return "Fichier CSS introuvable dans le dossier static/", 404

# --- VÉRIFICATION ET LIAISON ---

@app.route('/verify_level0', methods=['POST'])
def verify_level0():
    # On accepte 0610 ou 06:10 en enlevant les ":"
    user_input = request.form.get('code', '').replace(":", "")
    
    if user_input == "0610":
        return redirect('/level1') # Redirige vers le Level 1
    else:
        # Renvoie la page avec un message d'erreur intégré
        return render_template('level0exploration.html', error="CODE ERRONÉ. RÉALITÉ INSTABLE.")

# --- ROUTES DU LEVEL 1 ---

@app.route('/level1')
def level1():
    return render_template('level1.html')

@app.route('/level2')
def level2():
    return render_template('level2.html')

@app.route('/level3')
def level3():
    return render_template('level3.html')

@app.route('/level4')
def level4():
    return render_template('level4.html')

@app.route('/level5')
def level5():
    return render_template('level5.html')

if __name__ == '__main__':
    app.run(debug=True)