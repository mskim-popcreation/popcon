# coding: utf-8
from runserver import db

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Example(db.Model):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True)
    data = Column(String(45))


class Image(db.Model):
    __tablename__ = 'images'

    idimages = Column(Integer, primary_key=True)
    cat1 = Column(String(45))
    cat2 = Column(String(45))
    cat3 = Column(String(45))
    cat4 = Column(String(45))
    key1 = Column(String(45))
    key2 = Column(String(45))
    key3 = Column(String(45))
    key4 = Column(String(45))
    filename = Column(String(45))
    upload_date = Column(Date)
    db_show = Column(String(1), server_default=FetchedValue())
    folder1 = Column(String(45))
    folder2 = Column(String(45))
    folder3 = Column(String(45))
    onlyfilename = Column(String(45))
    onlyfiletype = Column(String(45))
    ranking = Column(String(45), server_default=FetchedValue())


class Order(Base):
    __tablename__ = 'order'

    idorder = Column(Integer, primary_key=True)
    order_date = Column(String(45))
    order_kind = Column(String(45))
    order_design_kind = Column(String(45))
    order_design_ratio = Column(String(45))
    order_design_memo = Column(String(45))
    order_quantity = Column(String(45))
    order_material = Column(String(45))
    order_size = Column(String(45))
    order_finishing = Column(String(45))
    order_additional = Column(String(45))
    order_pacakge = Column(String(45))
    order_request = Column(String(45))
    order_installation = Column(String(45))
    order_price = Column(String(45))
    status_design = Column(String(45))
    status_print = Column(String(45))
    status_finish = Column(String(45))
    status_deliever = Column(String(45))
    iduser = Column(Integer)


class Product(Base):
    __tablename__ = 'product'

    idproduct = Column(Integer, primary_key=True)
    name = Column(String(45))
    material = Column(String(45))
    ink = Column(String(45))
    quality = Column(String(45))
    standard = Column(String(45))
    unit = Column(String(45))
    per1 = Column(String(45))
    per9 = Column(String(45))
    per49 = Column(String(45))
    per99 = Column(String(45))
    per100 = Column(String(45))


class User(Base):
    __tablename__ = 'users'

    idusers = Column(Integer, primary_key=True)
    email = Column(String(45))
    password = Column(String(200))
    joindate = Column(Date)
