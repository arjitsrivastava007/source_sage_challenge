from sqlalchemy import create_engine, Column, Integer, String, Boolean, \
     ForeignKey, Numeric, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:@localhost:5432/backend')
# engine = create_engine('mysql+pymysql://user:pass@db_host/dbname')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(name='Model')


class Image(Base):
    __tablename__ = "images"
    id = Column('image_id', Integer, primary_key=True)
    url = Column(String(100))


class Products(Base):
    __tablename__ = 'products'
    id = Column('product_id', Integer, primary_key=True)
    name = Column(String(32))
    description = Column(String(50))
    images = Column(Integer)
    logo_id = Column(Image, ForeignKey('images.image_id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Variants(Base):
    __tablename__ = "variants"
    id = Column('variant_id', Integer, primary_key=True)
    product_id = Column(Products, ForeignKey('products.product_id'))
    name = Column(String(32))
    size = Column(Numeric)
    color= Column(String(32))
    images = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

