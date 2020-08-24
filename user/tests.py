import json

from django.test  import TestCase, Client

from.models       import User

client = Client()

class JustTest(TestCase):

    def test_user_signup(self):
        data = {
               'account'               :'testid127',
               'password'              :'testPsswoed1!',
               'name'                  :'김태하',
               'phone'                 :'010-2997-6673',
               'email'                 :'test@test.com',
               'birthday'              :'19921104',
               'sms_marketing_agree'   :'False',
               'email_marketing_agree' :'False'
        }
       
        response = client.post('/user/signup', json.dumps(data), content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
           "message": 'Success'
        })

if __name__ == '__main__':
    unittest.main()