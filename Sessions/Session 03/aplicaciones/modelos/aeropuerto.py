from aplicaciones import db

class Aeropuerto(db.Model):
    idaeropuerto = db.Column(db.Integer, primary_key = True)
    aeropuerto = db.Column(db.String(60), nullable = False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.idpais', ondelete='CASCADE'))
    ciudad = db.Column(db.String(45), nullable = False)

    def __init__(self, aeropuerto, pais_id, ciudad) -> None:
        self.aeropuerto = aeropuerto
        self.pais_id = pais_id
        self.ciudad = ciudad
    
    def __str__(self) -> str:
        return self.aeropuerto
