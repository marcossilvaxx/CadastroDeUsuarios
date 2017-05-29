from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = "usuario"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<User %s>" % nome

db.create_all()

@app.route("/user", methods=["GET", "POST"])
@app.route("/user/<int:id>", methods=["PUT","DELETE"])
def user(id=None):
    if request.method == "GET":
        usuarios = Usuario.query.all()
        response = make_response(jsonify(usuarios))
        return response
    elif request.method == "POST":
        usuario = request.json
        u = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
        db.session.add(u)
        db.session.commit()
        return ""
    elif request.method == "PUT":
        usuario = request.json
        usuarioAntigo = Usuario.query.filter_by(_id=id).first()

        if usuario.nome and usuario.email and usuario.senha:
            usuarioAntigo.nome = usuario.nome
            usuarioAntigo.email = usuario.email
            usuarioAntigo.senha = usuario.senha

            db.session.commit()

            return "", 200

        return ""
    elif request.method == "DELETE":
        usuario = Usuario.query.filter_by(_id=id).first()

        db.session.delete(usuario)
        db.session.commit()

        return ""

app.run(debug=True, use_reloader=True)

#Falta colocar os Headers de ALLOW-SAME-ORIGIN
