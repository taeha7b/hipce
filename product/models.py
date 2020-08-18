from django.db import models

class Category(models.Model):

    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'categories'

class Collection(models.Model):
    name= models.CharField(max_length=50)
    image = models.CharField(max_length=50)

    class Meta:
        db_table = 'collections'

class Product(models.Model):
    category    = models.ForeignKey(Category, on_delete = models.CASCADE)
    name        = models.CharField(max_length = 50)
    detail_view = models.CharField(max_length = 5000)
    price       = models.CharField(max_length = 50)
    collection = models.ForeignKey(Collection, on_delete= CASCADE)
    image=models.ForeignKey(Image, on_delete= CASCADE)

    class Meta:
        db_table = 'products'


class Color(models.Model):
    name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product)
    class Meta:
        db_table = 'colors'


class Image(models.Model):
    main=models.CharField(max_length=500)
    sub_main = models.CharField(max_lenngth=500)
    inner    = models.CharField(max_length=500)
    bascket  = models.CharField(max_length=500)

    class Meta:
        db_table = 'images'



class Special(models.Model):
    new_image=modles.CharField(max_length=500)
    discount_image=models.CharField(max_length=500)
    sold_out_image=models.CharField(max_length=500)
    limited_image=models.CharField(max_length=500)
    product= models.ManyToManyField(Product)

    class  META:
        db_rabel= 'image'



