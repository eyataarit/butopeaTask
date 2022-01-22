from peewee import *

class ProductImage (Model):
    product_image_id=TextField()
    product_id=TextField()
    image=TextField()
    sort_order=IntegerField()