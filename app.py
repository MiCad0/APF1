from flask import Flask, request, jsonify

#Creer l'app flask
app = Flask(__name__)

# Initialiser SQLAlchemy
db = SQLAlchemy(app)



@app.route('/')
def home():
    return 'Hello World!'

#Activer mode Debug pour voir les erreur et recharger automatiquement le serveur
if __name__ == '__main__':
    app.run(debug=True)