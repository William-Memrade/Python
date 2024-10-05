from aplicaciones import db

class Pais(db.Model):

    idpais = db.Column(db.Integer, primary_key = True)
    pais = db.Column(db.String(50), nullable = False)

    usuarios = db.relationship('Usuario', backref='idpais', lazy=True)
    usuarios = db.relationship('Aeropuerto', backref='idpais', lazy=True)

    def __init__(self, pais) -> None:
        self.pais = pais
