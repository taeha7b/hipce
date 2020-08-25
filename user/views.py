import bcrypt, json, jwt, re

from django.views    import View
from django.http     import JsonResponse

from .models         import User
from .validation     import ValidationError
from hince.settings  import SECRET_KEY, ALGORITHM

class SignUp(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            regex = re.compile(r'^(?=.*[a-zA-Z0-9])(?=.*[a-zA-Z!@#$%^&*])(?=.*[0-9!@#$%^&*]).{10,16}')
            if not regex.match(data['password']):
                return JsonResponse({"MESSAGE": "RIGHT PASSWORD REQUIRED"}, status = 400)
            
            encode_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            user = User(
                    account                  = data['account'],
                    password                 = encode_password.decode('utf-8'),
                    name                     = data['name'],
                    phone                    = data['phone'],
                    email                    = data['email'],
                    birthday                 = data['birthday'],
                    is_sms_marketing_agree   = data['sms_marketing_agree'],
                    is_email_maketing_agree  = data['email_marketing_agree'],
            )
            user.full_clean()
            user.save()
            return JsonResponse({"MESSAGE": "SUCCESS"}, status = 200)
            
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

class SignIn(View):
    def post(self, request): 
        try:  
            data = json.loads(request.body)
            if data['password']=="":
                return JsonResponse({"MESSAGE": "Please enter your password"})

            if User.objects.filter(account = data['account']).exists():
                user = User.objects.get(account = data['account'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({'ID' : user.id}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
                    return JsonResponse({"TOKEN": access_token}, status = 200)
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status = 401)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)

class LoginConfirm:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, request):
        TOKEN = request.headers.get("Authorization", None)
        try:
            if TOKEN:
                token_payload = jwt.decode(TOKEN, SECRET_KEY['secret'], ALGORITHM['algorithm'])
                user_id       = User.objects.get(id = token_payload['id'])
                request.user  = user_id
                return self.original_function(self, request)
            return JsonResponse({'MESSAGE':'LOGIN_REQUIRED'}, status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'MESSAGE':'EXPIRED_TOKEN'}, status=401)

        except jwt.DecodeError:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=401)