from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'categories'

class Collection(models.Model):
    name  = models.CharField(max_length = 50)
    image = models.URLField(max_length = 500)
    video = models.URLField(max_length = 500)

    class Meta:
        db_table = 'collections'

class Product(models.Model):
    category          = models.ForeignKey('Category', on_delete = models.CASCADE)
    name              = models.CharField(max_length = 50)
    description_image = models.URLField(max_length = 5000)
    price             = models.DecimalField(max_digits = 6, decimal_places = 4)
    collection        = models.ForeignKey('Collection', on_delete = models.CASCADE)
    stock             = models.IntegerField(default=0)
    tag               = models.ManyToManyField('Tag', through = 'ProductTag')
    color             = models.ManyToManyField('Color', through = 'ProductColor')

    class Meta:
        db_table = 'products'
        
class ProductTag(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    tag     = models.ForeignKey('Tag', on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'products_tags'

class Tag(models.Model):
    new_product            = models.CharField(max_length = 500)
    discount_event_product = models.CharField(max_length = 500)
    sold_out_product       = models.CharField(max_length = 500)
    limited_product        = models.CharField(max_length = 500)

    class Meta:
        db_table = 'tags'

class ProductColor(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    color   = models.ForeignKey('Color', on_delete = models.CASCADE)

    class Meta:
        db_table = 'products_colors'

class Color(models.Model):
    name    = models.CharField(max_length = 50)
    
    class Meta: 
        db_table = 'colors'

class Image(models.Model):
    url        = models.URLField(max_length = 500)
    image_type = models.ForeignKey('ImageType', on_delete = models.CASCADE)
    product    = models.ForeignKey('Product', on_delete = models.CASCADE)

    class Meta:
        db_table = 'images'

class ImageType(models.Model):
    name = models.CharField(max_length = 500)

    class Meta:
        db_table = 'image_types'