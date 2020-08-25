from django.db import models

from .validation import (
    validate_account,
    validate_name,
    validate_phone
)

class User(models.Model):
    account                 = models.CharField(max_length  = 50, validators = [validate_account], unique = True)
    password                = models.CharField(max_length  = 256)
    name                    = models.CharField(max_length  = 50, validators = [validate_name])
    phone                   = models.CharField(max_length  = 50, validators = [validate_phone])
    email                   = models.EmailField(max_length = 50, unique = True)
    birthday                = models.DateField(max_length  = 50)
    is_sms_marketing_agree  = models.BooleanField(default  = False, blank = True)
    is_email_maketing_agree = models.BooleanField(default  = False, blank = True)
    
    class Meta:
        db_table = 'users'