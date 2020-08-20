from django.views import View
from django.http import JsonResponse
from .models import User
from .validation import ValidationError
from hince.settings import SECRET_KEY
import bcrypt
import json
import jwt
import re

class SignUp(View):
    def post(self, request):

        data = json.loads(request.body)

        try:

            regex = re.compile(r'^(?=.*[a-zA-Z0-9])(?=.*[a-zA-Z!@#$%^&*])(?=.*[0-9!@#$%^&*]).{10,16}')

            if not regex.match(data['password']):
                return JsonResponse({"message": "right password required"}, status=400)

            encode_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            user = User(
                account                 = data['account'],
                password                = encode_password.decode('utf-8'),
                name                    = data['name'],
                phone                   = data['phone'],
                email                   = data['email'],
                birthday                = data['birthday'],
                is_sms_marketing_agree  = data['sms_marketing_agree'],
                is_email_maketing_agree = data['email_marketing_agree'],
            )

            user.full_clean()
            user.save()

            return JsonResponse({"message": "Success"}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
