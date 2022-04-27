from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
import unittest


class TestBase(TestCase):
    '''Test de correspondencia de url a template y registro'''
    def setUp(self):
        
        self.register_url=reverse("register")
        self.user={

            'email': 'user@example.com',
            'username': 'username',
            'password1':'password123',
            'password2':'password123',


        }

        return super(). setUp()

class RegisterTest(TestBase):
    def test_view(self):
        respuesta= self.client.get(self.register_url) 
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta,"appblog/register.html")


    def test_register(self):
        
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)


class TestLogin(TestCase):
    ''''test correspondencia template login'''
    def setUp(self):
        self.login_url=reverse("login")
        return super(). setUp()

class TestLog(TestLogin):
    def test_login_request(self):
        respuesta1= self.client.get(self.login_url)  
        self.assertEqual(respuesta1.status_code, 200)
        self.assertTemplateUsed(respuesta1,"appblog/login.html")    





