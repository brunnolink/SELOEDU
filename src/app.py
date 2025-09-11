from flask import Flask, render_template

app = Flask(__name__)
 
users = [
    {"id": 1, "name": "Jose Mauricio", "email": "joseMauricio@email.com", "perfil": "Professor", "status": "Ativo"},
    {"id": 2, "name": "Brunno", "email": "brunno@email.com", "perfil": "Estudante", "status": "Inativo"},
    {"id": 3, "name": "Carla", "email": "carla@email.com", "perfil": "Professor", "status": "Ativo"},
    {"id": 4, "name": "Daniel", "email": "daniel@email.com", "perfil": "Estudante", "status": "Ativo"},
    {"id": 5, "name": "Eduarda", "email": "eduarda@email.com", "perfil": "Admin", "status": "Inativo"},
    {"id": 6, "name": "Felipe", "email": "felipe@email.com", "perfil": "Estudante", "status": "Ativo"},
    {"id": 7, "name": "Gabriela", "email": "gabriela@email.com", "perfil": "Professor", "status": "Ativo"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def listar_usuarios():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)