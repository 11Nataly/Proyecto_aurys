from .database import Base #el punto en .database,sirve para llamar un cosas dentro del paquete 
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Categoria(Base):#crear la clase para la tabla
    __tablename__ = "categorias" #nombre de la tabla
    id = Column(Integer ,
                primary_key=True)                          
    nombre=Column(String(60))
    
    
class Jovenes(Base):
    __tablename__ = "jovenes"
    id = Column(Integer,
                primary_key=True)
    nombre= Column(String(60))
    apellido= Column(String(60))
    correo= Column(String(60))
    foto= Column(String(60))
    fecha_registro= Column(Date)
    
    #relacion uno a muchos con emociones
    emociones = relationship("Emociones" ,
                             back_populates="jovenes")
    
    
    
class Emociones(Base):
    __tablename__ = "emociones"
    id = Column(Integer,
                primary_key=True)
    descripcion= Column(String(60))
    fecha_registro= Column(Date)
    
     #clave foranea
    jovenes_id =Column(Integer,
                       ForeignKey("jovenes.id"))
    
class TiposEmocion(Base):
    __tablename__ = "tipos_emocion"
    id = Column(Integer,
                primary_key=True)
    nombre= Column(String(60))
    

    

    
    
    

    
    
    #migraciones: cambios que se van a hacer en la base de datos
    