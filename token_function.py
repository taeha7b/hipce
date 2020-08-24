import bcrypt, json, jwt, re

from django.http     import JsonResponse

from hince.settings  import SECRET_KEY
from user.models     import User

def make_token(account,password):
    if bcrypt.checkpw(password.encode('utf-8'), User.objects.get(account = account).password.encode('utf-8')):
        access_token = jwt.encode({'ID' : User.objects.get(account = account).id}, SECRET_KEY['secret'], algorithm = 'HS256').decode('utf-8')
        return JsonResponse({"TOKEN": access_token}, status = 200)