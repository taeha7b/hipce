import json, jwt

from django.views    import View
from django.http     import JsonResponse

from .models         import User
from hince.settings  import SECRET_KEY, ALGORITHM

def login_confirm(original_function):
    def wrapper(self, request):
        try:
            access_token = request.headers.get("Authorization", None)
            if access_token:
                token_paylod    = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])
                request.account = User.objects.get(id = token_paylod['USER_ID'])
                return original_function(self, request)
            return JsonResponse({'MESSAGE':'LOGIN_REQUIRED'}, status = 401)

        except jwt.DecodeError:
            return JsonResponse({'MESSAGE':'INVALID_USER1'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER2'}, status = 401)

    return wrapper
