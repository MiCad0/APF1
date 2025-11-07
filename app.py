from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#Creer l'app flask
app = Flask(__name__)

#Confi de la BDD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialiser SQLAlchemy
db = SQLAlchemy(app)

#Def classe student de la BDD
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)


@app.route('/')
def home():
    return 'Hello World!'

#Activer mode Debug pour voir les erreur et recharger automatiquement le serveur
if __name__ == '__main__':
    app.run(debug=True)