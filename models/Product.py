from peewee import *
from 'Connection.py' import connect

class Product (Model):
    product_id=TextField()
    model=TextField()
    ean=TextField()
    quantity=IntegerField()
    image=TextField()
    manufacturer_id=TextField()
    price=DecimalField()
    status=IntegerField()


    class Meta:
        database=db
        db_table='User'