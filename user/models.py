from django.db import models


from .validation import validate_account
from .validation import validate_birthday
from .validation import validate_email
from .validation import validate_name
from .validation import validate_phone

class User(models.Model):
    account                 = models.CharField(max_length = 50, validators = [validate_account], unique = True)
    password                = models.CharField(max_length = 256)
    name                    = models.CharField(max_length = 50, validators = [validate_name])
    phone                   = models.CharField(max_length = 50, validators = [validate_phone])
    email                   = models.EmailField(max_length = 50, validators = [validate_email], unique = True)
    birthday                = models.DateField(max_length = 50, validators = [validate_birthday])
    is_sms_marketing_agree  = models.BooleanField(default = False, blank = True)
    is_email_maketing_agree = models.BooleanField(default = False, blank = True)
    
    class Meta:
        db_table= 'users'


class ShippingDestination:
    destination_ninkname = models.CharField(max_length = 50)
    name                 = models.CharField(max_length = 50)
    address              = models.CharField(max_length = 500)
    phone                = models.CharField(max_length = 50)
    is_main_destination  = models.BooleanField(default = False)
    user                 = models.ForeignKey('User', on_delete = models.CASCADE)

    class Meta:
        db_table = 'shipping_destinations'

