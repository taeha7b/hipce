from django.db import models

class Category(models.Model):

    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'categories'

class Collection(models.Model):

    name  = models.CharField(max_length = 50)
    image = models.CharField(max_length = 500)
    video = models.CharField(max_length = 500)

    class Meta:
        db_table = 'collections'

class Product(models.Model):

    category          = models.ForeignKey(Category, on_delete = models.CASCADE)
    name              = models.CharField(max_length = 50)
    description_image = models.CharField(max_length = 5000)
    price             = models.CharField(max_length = 50)
    collection        = models.ForeignKey(Collection, on_delete = CASCADE)
    stock             = models.CharField(max_length = 50)
    tag               = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'products'


class Color(models.Model):

    name    = models.CharField(max_length = 50)
    product = models.ManyToManyField(Product)
    
    class Meta: 
        db_table = 'colors'


class Image(models.Model):

    url        = models.CharField(max_length = 500)
    image_type = models.ForeignKey(image_types, on_delete = CASCADE)
    product    = models.ForeignKry(Product, on_delete = CASCADE)

    class Meta:
        db_table = 'images'


class Tag(models.Model):

    new_product            = models.CharField(max_length = 500)
    discount_event_product = models.CharField(max_length = 500)
    sold_out_product       = models.CharField(max_length = 500)
    limited_product        = models.CharField(max_length = 500)

    class Meta:
        db_table = 'tags'

class image_type(models.Model):
    name = models.CharField(max_length = 500)

    class Meta:
        db_table = 'image_types'