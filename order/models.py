from django.db import models

class ShoppingBag(models.Model):
    user        = models.ForeignKey('user.User', on_delete = models.CASCADE)
    product     = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    quantity    = models.PositiveIntegerField(default = 0)
    total_price = models.PositiveIntegerField(default = 0)
