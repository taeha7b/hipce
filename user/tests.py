from django.test import TestCase, Client
from.models import User
import json

client = Client()

class JustTest(TestCase):


    def test_user_signup(self):
        data = {'account':'testid127', 'password':'testPsswoed1!', 'name':'김태하', 'phone':'010-2997-6673', 
        'email':'test@test.com', 'birthday':'19921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'False'}
       
        response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
           "message": 'Success'
        })

    # def test_user_signup_account(self):
    #     data = {'account':'te', 'password':'testPsswoed1!', 'name':'김태하', 'phone':'010-2997-6673', 'email':'test@test.com', 'birthday':'19921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'False'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })

    # def test_user_signup_password(self):
    #     data = {'account':'testid123', 'password':'t!', 'name':'김태하', 'phone':'010-2997-6673', 'email':'test@test.com', 'birthday':'19921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'False'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })

    # def test_user_signup_name(self):
    #     data = {'account':'testid123', 'password':'testPsswoed1!', 'name':'김태하123', 'phone':'010-2997-6673', 'email':'test@test.com', 'birthday':'19921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'False'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })

    # def test_user_signup_phone(self):
    #     data = {'account':'testid123', 'password':'testPsswoed1!', 'name':'김태하', 'phone':'0103-29937-66713', 'email':'test@test.com', 'birthday':'19921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'False'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })
        
    # def test_signup_email(self):
    #     data = {'account':'testid123', 'password':'testPsswoed1!', 'name':'김태하', 'phone':'010-2997-6673', 'email':'test.com', 'birthday':'19921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'False'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })

    # def test_signup_birthday(self):
    #     data = {'account':'testid123', 'password':'testPsswoed1!', 'name':'김태하', 'phone':'010-2997-6673', 'email':'test@test.com', 'birthday':'921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'False'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })

    # def test_signup_sms_marketing_agree(self):
    #     data = {'account':'testid123', 'password':'testPsswoed1!', 'name':'김태하', 'phone':'010-2997-6673', 'email':'test@test.com', 'birthday':'19921104', 'sms_marketing_agree':'123', 'email_marketing_agree':'False'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })

    # def test_signup_email_marketing_agree(self):
    #     data = {'account':'testid123', 'password':'testPsswoed1!', 'name':'김태하', 'phone':'010-2997-6673', 'email':'test@test.com', 'birthday':'19921104', 'sms_marketing_agree':'False', 'email_marketing_agree':'123'}
       
    #     response = client.post('/user/signup', json.dumps(data), content_type='application/json') 
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), {
    #        "message": 'Success'
    #     })

if __name__ == '__main__':
    unittest.main()