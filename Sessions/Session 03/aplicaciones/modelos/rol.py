from aplicaciones import db

class Rol(db.Model):

    idrol = db.Column(db.Integer, primary_key = True)
    rol = db.Column(db.String(50), nullable = False)

    usuarios = db.relationship('Usuario', backref='rol', lazy=True)

    def __init__(self, rol) -> None:
        self.rol = rol
