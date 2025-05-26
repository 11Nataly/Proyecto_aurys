#trae la clase base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#CONNECTION STRING
#representa la base de datos a conectarse
#depende de la base de datos que se use
#y el lenguaje de programación
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:admin@localhost:3315/aurys_3147234'

#Crear el objetivo de conexion
conn = create_engine(SQLALCHEMY_DATABASE_URL)

#lA CLASE BASE PARA LOS MODELOS
Base = declarative_base()