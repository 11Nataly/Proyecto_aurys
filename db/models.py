from .database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Float, Text
from sqlalchemy.orm import relationship

# Modelos del primer diagrama
class Jovenes(Base):
    __tablename__ = 'jovenes'
    id_jovenes = Column(Integer, primary_key=True)
    nombre_jovenes = Column(String(60))
    apellido_jovenes = Column(String(60))
    correo_jovenes = Column(String(100))
    foto_jovenes = Column(String(255))

    # Relaciones
    notas_diario = relationship("NotasDiario", back_populates="joven")
    notas_temporales = relationship("NotasDiarioTemporal", back_populates="joven")
    emociones = relationship("Emociones", back_populates="joven")
    promesas = relationship("Promesa", back_populates="joven")
    notas_voz = relationship("NotasVoz", back_populates="joven")
    frecuencias = relationship("Frecuencia", back_populates="joven")
    red_apoyo = relationship("RedApoyo", back_populates="joven")
    motivaciones = relationship("Motivaciones", back_populates="joven")

   
class NotasDiarioTemporal(Base):
    __tablename__ = 'notas_diario_temporal'
    id_notas_temp = Column(Integer, primary_key=True)
    pin_notas_temp = Column(Boolean, default=False)
    titulo_notas_temp = Column(String(100))
    descripcion_notas_temp = Column(Text)
    texto_notas_temp = Column(Text)
    fecha_notas_temp = Column(Date)
    fk_id_joven_temp = Column(Integer, ForeignKey('jovenes.id_jovenes'))
    fecha_creacion_temp = Column(Date)

    joven = relationship("Jovenes", back_populates="notas_temporales")


 
class NotasDiario(Base):
    __tablename__ = 'notas_diario'
    id_notas = Column(Integer, primary_key=True)
    pin_notas = Column(Boolean, default=False)
    titulo_notas = Column(String(100))
    descripcion_notas = Column(Text)
    texto_notas = Column(Text)
    fecha_notas = Column(Date)
    fk_id_joven = Column(Integer, ForeignKey('jovenes.id_jovenes'))

    joven = relationship("Jovenes", back_populates="notas_diario")

class TiposEmocion(Base):
    __tablename__ = 'tipos_emocion'
    id_tipo_emociones = Column(Integer, primary_key=True)
    nombre_tipo_emocion = Column(String(60))

    emociones = relationship("Emociones", back_populates="tipo")


class Frecuencia(Base):
    __tablename__ = 'frecuencia'
    id_frecuencia = Column(Integer, primary_key=True)
    severidad_frecuencia = Column(String(50))
    duracion = Column(String(50))
    fk_id_joven = Column(Integer, ForeignKey('jovenes.id_jovenes'))

    joven = relationship("Jovenes", back_populates="frecuencias")


class NotasVoz(Base):
    __tablename__ = 'notas_voz'
    id_Notas_voz = Column(Integer, primary_key=True)
    Nombre_notas_voz = Column(String(100))
    Fecha_notas_voz = Column(Date)
    duracion_notas_voz = Column(Float)
    Descripcion_notas_voz = Column(Text)
    fk_id_joven = Column(Integer, ForeignKey('jovenes.id_jovenes'))

    joven = relationship("Jovenes", back_populates="notas_voz")

    
class Promesa(Base):
    __tablename__ = 'promesa'
    id_promesa = Column(Integer, primary_key=True)
    titulo_promesa = Column(String(100))
    Descripcion_promesa = Column(Text)
    Fecha_creacion = Column(Date)
    Fecha_cumplimiento = Column(Date, nullable=True)
    fk_id_joven = Column(Integer, ForeignKey('jovenes.id_jovenes'))

    joven = relationship("Jovenes", back_populates="promesas")



class Emociones(Base):
    __tablename__ = 'emociones'
    id_emociones = Column(Integer, primary_key=True)
    descripcion_emocion = Column(Text)
    fecha_emociones = Column(Date)
    fk_tipo_emociones = Column(Integer, ForeignKey('tipos_emocion.id_tipo_emociones'))
    fk_id_joven = Column(Integer, ForeignKey('jovenes.id_jovenes'))

    joven = relationship("Jovenes", back_populates="emociones")
    tipo = relationship("TiposEmocion", back_populates="emociones")

  
class RedApoyo(Base):
    __tablename__ = 'red_apoyo'
    id_red_apoyo = Column(Integer, primary_key=True)
    nombre_red_apoyo = Column(String(60))
    apellido_red_apoyo = Column(String(60))
    telefono_red_apoyo = Column(String(20))
    relacion_red_apoyo = Column(String(50))
    descripcion_red_apoyo = Column(Text)
    fecha_red_apoyo = Column(Date)
    fk_id_joven = Column(Integer, ForeignKey('jovenes.id_jovenes'))

    joven = relationship("Jovenes", back_populates="red_apoyo")

    
# Modelos del segundo diagrama
class Categorias(Base):
    __tablename__ = 'categories'
    id_categoria = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(60))
    description_categoria = Column(Text)
    fecha_creacion_cate = Column(Date)

    motivaciones = relationship("Motivaciones", back_populates="categoria")

    
class FavoritasMotivaciones(Base):
    __tablename__ = 'favoritas_motivaciones'
    id_favorite_motivac = Column(Integer, primary_key=True)
    nombre_favorite_mt = Column(String(100))

    motivaciones = relationship("Motivaciones", back_populates="favorito")

   
class TecnicasAfrontamiento(Base):
    __tablename__ = 'recnicas'  # Nota: El nombre parece tener un error tipográfico
    id_Afrontamiento_e = Column(Integer, primary_key=True)
    FK_calification_Afront = Column(Integer)
    FK_favorito_Afronta = Column(Integer, ForeignKey('favorites_tecnicas.id_favorite_afrontan'))

    favorito = relationship("FavoritesTecnicas", back_populates="tecnicas")

    
class FavoritesTecnicas(Base):
    __tablename__ = 'favorites_tecnicas'
    id_favorite_afrontan = Column(Integer, primary_key=True)
    nombre_favorite_aft = Column(String(100))

    tecnicas = relationship("TecnicasAfrontamiento", back_populates="favorito")

   
class Motivaciones(Base):
    __tablename__ = 'motivaciones'
    id_Recuerdo = Column(Integer, primary_key=True)
    nombre_Recuerdo = Column(String(100))
    description_Recuerdo = Column(Text)
    fecha_creacion_Rec = Column(Date)
    foto_Recuerdo = Column(String(255))
    fk_id_joven = Column(Integer, ForeignKey('jovenes.id_jovenes'))
    FK_id_Favoritos_motivac = Column(Integer, ForeignKey('favoritas_motivaciones.id_favorite_motivac'))
    FK_id_categoria = Column(Integer, ForeignKey('categories.id_categoria'))

    joven = relationship("Jovenes", back_populates="motivaciones")
    favorito = relationship("FavoritasMotivaciones", back_populates="motivaciones")
    categoria = relationship("Categorias", back_populates="motivaciones")

   


    

    
    
    

    
    
    #migraciones: cambios que se van a hacer en la base de datos
    