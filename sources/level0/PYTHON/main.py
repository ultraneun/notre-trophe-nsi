from flask import Flask

app = Flask("Backrooms")

@app.route('/') 
def index(): 
    return "<p>Tout fonctionne parfaitement</p>" 

app.run(debug=True)
