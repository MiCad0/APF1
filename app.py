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

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

#Racine de l'API pour verifier que le serveur fonctionne
@app.route('/')
def home():
    return 'Hello World!'

#Endpoint pour lister tous les étudiant
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify(list(map(Student.to_dict,students))), 201
    

#Ajouter un nouvel etudiant (methode POST)
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

#Affichier un étudiant sachant son ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    if student:
        return jsonify(student.to_dict())
    return jsonify({'error': 'Etudiant non trouvé'}), 404

#Mettre a jour un etudiant (methode PUT)
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Etudiant non trouvé'}), 404
    
    data = request.get_json()
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    db.session.commit()
    return jsonify(student.to_dict())

#Supprimer un etudiant (methode DELETE)
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'error': 'Etudiant non trouvé'}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Etudiant supprimé'}), 200



#Activer mode Debug pour voir les erreur et recharger automatiquement le serveur
# Activation des bdd
if __name__ == '__main__':
    with app.app_context():
        # db.init_app(app)
        db.create_all()
    app.run(debug=True)