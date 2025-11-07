from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#Creer l'app flask
app = Flask(__name__)

#Config de la BDD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialiser SQLAlchemy
db = SQLAlchemy(app)

#Def classe student de la BDD
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

#Racine de l'API pour verifier que le serveur fonctionne
@app.route('/')
def home():
    return 'Hello World!'

#Endpoint pour lister tous les étudiant

#Ajouter un nouvel etudiant (methode POST)
@app.route('/students', methods=['POST'])

#Affichier un étudiant sachant son ID
@app.route('/students/<int:id>', methods=['GET'])

#Mettre a jour un etudiant (methode PUT)
@app.route('/students/<int:id>', methods=['PUT'])

#Supprimer un etudiant (methode DELETE)
@app.route('/students/<int:id>', methods=['DELETE'])



#Activer mode Debug pour voir les erreur et recharger automatiquement le serveur
if __name__ == '__main__':
    app.run(debug=True)