from peewee import *

class ProductDescription (Model):
    product_id=TextField()
    name=TextField()
    description=TextField()