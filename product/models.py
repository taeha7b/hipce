from django.db import models

class Category(models.Model):
    name  = models.CharField(max_length = 50)
    image = models.URLField(max_length = 5000)

    class Meta:
        db_table = 'categories'

class Collection(models.Model):
    name  = models.CharField(max_length = 255)
    image = models.URLField(max_length = 500)
    video = models.URLField(max_length = 500)

    class Meta:
        db_table = 'collections'

class Product(models.Model):
    category          = models.ForeignKey('Category', on_delete = models.CASCADE)
    name              = models.CharField(max_length = 50)
    main_image        = models.URLField(max_length = 500)
    sub_image         = models.URLField(max_length = 500)
    description_image = models.URLField(max_length = 5000)
    price             = models.DecimalField(max_digits = 20, decimal_places = 4)
    collection        = models.ForeignKey('Collection', on_delete = models.CASCADE)
    tag               = models.URLField(max_length = 5000)
    color             = models.ManyToManyField('Color', through = 'ProductColor')

    class Meta:
        db_table = 'products'

class ProductColor(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    color   = models.ForeignKey('Color', on_delete = models.CASCADE)

    class Meta:
        db_table = 'products_colors'

class Color(models.Model):
    name    = models.CharField(max_length = 50)
    
    class Meta: 
        db_table = 'colors'