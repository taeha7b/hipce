from django.db import models

class Store(models.Model):
    name         = models.CharField(max_length = 200)
    address      = models.CharField(max_length = 256)
    business_day = models.CharField(max_length = 50, blank = True, null = True)
    opening_hour = models.CharField(max_length = 50)
    contact      = models.CharField(max_length = 50)

    class Meta:
        db_table = 'stores'