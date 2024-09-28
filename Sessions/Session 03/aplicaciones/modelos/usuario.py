from aplicaciones import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    idusuario = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(50), nullable = False)
    nombres = db.Column(db.String(50), nullable = False)
    apellidos = db.Column(db.String(50), nullable = False)
    correo = db.Column(db.String(100), nullable = False)
    clave = db.Column(db.String(250), nullable = False)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.idrol', ondelete='CASCADE'))

    def __init__(self, usuario, nombres, apellidos, correo , clave, rol_id) -> None:
        self.usuario = usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.clave = generate_password_hash(clave)
        self.rol_id = rol_id
    
    def __str__(self) -> str:
        return self.usuario
