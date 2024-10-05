class BaseConfig:
    'Base configuracion'
    SECRET_KEY = 'ClaveMasDificil'
    DEBUG = True
    TESTING = False
    ENV = "development"

class ProductionConfig(BaseConfig):
    #Produccion configuracion
    DEBUG = False
    ENV = "production"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://aerouser:Clav3M45Dificil@192.168.1.20:1433/aerolinea"

class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    # DEBUG = True
    TESTING = True
    # ENV = "development"
    SECRET_KEY = '123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:WilliamMemrade2!@localhost/aerolinea"
    # SQLALCHEMY_DATABASE_URI = "mssql+pymssql://sa:admin@192.168.1.20:1433/aerolinea"
