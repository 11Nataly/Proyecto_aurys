#trae la clase base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#variable que representa conexión con base de datos en maria db
SQLALCHEMY_DATABASE_URI = 'mariadb://root@admin/localhost:3315/py-shopy'