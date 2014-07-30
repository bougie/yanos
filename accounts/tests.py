import json

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from lib.exception import CoreException
from .core.register import coreRegister
from .core.login import coreLogin


class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='existinguser', password='fubar')

    def test_url_registering_url_success(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)

    def test_ajaxurl_registering_url_success(self):
        response = self.client.get(
            '/accounts/register',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_registering_bad_password_failed(self):
        try:
            coreRegister('username', 'p1', 'p0')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_url_registering_bad_password_failed(self):
        args = {
            'username': 'username',
            'password': 'p1',
            'password2': 'p3'
        }
        response = self.client.post('/accounts/register', args)
        self.assertEqual(response.status_code, 200)

    def test_ajaxurl_registering_bad_password_failed(self):
        args = {
            'username': 'username',
            'password': 'p1',
            'password2': 'p3'
        }
        response = self.client.post(
            '/accounts/register',
            args,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content.decode("UTF-8"))
        self.assertFalse(j['success'])

    def test_registering_existing_username_failed(self):
        try:
            coreRegister('existinguser', 'p1', 'p1')
        except CoreException as e:
            self.assertEqual(2, e.code)

    def test_url_registering_existing_username_failed(self):
        args = {
            'username': 'existinguser',
            'password': 'p1',
            'password2': 'p1'
        }
        response = self.client.post('/accounts/register', args)
        self.assertEqual(response.status_code, 200)

    def test_ajaxurl_registering_existing_username_failed(self):
        args = {
            'username': 'existinguser',
            'password': 'p1',
            'password2': 'p1'
        }
        response = self.client.post(
            '/accounts/register',
            args,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content.decode("UTF-8"))
        self.assertFalse(j['success'])

    def test_registering_success(self):
        coreRegister('pwet', 'camembert', 'camembert')

        self.assertEqual(2, User.objects.all().count())

    def test_url_registering_success(self):
        args = {
            'username': 'pwet',
            'password': 'camembert',
            'password2': 'camembert'
        }
        response = self.client.post('/accounts/register', args)
        # Rdirect to / when registering succeded
        self.assertEqual(response.status_code, 302)

    def test_ajaxurl_registering_success(self):
        args = {
            'username': 'pwet',
            'password': 'camembert',
            'password2': 'camembert'
        }
        response = self.client.post(
            '/accounts/register',
            args,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content.decode("UTF-8"))
        self.assertTrue(j['success'])

    def test_url_login_url_success(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)

    def test_ajaxurl_login_url_success(self):
        response = self.client.get(
            '/accounts/login',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_login_bad_username_failed(self):
        try:
            coreLogin(username='unexistinguser', password='pwet')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_url_login_bad_username_failed(self):
        args = {
            'username': 'unexistinguser',
            'password': 'pwet'
        }
        response = self.client.post('/accounts/login', args)
        self.assertEqual(response.status_code, 200)

    def test_ajaxurl_login_bad_username_failed(self):
        args = {
            'username': 'unexistinguser',
            'password': 'pwet'
        }
        response = self.client.post(
            '/accounts/login',
            args,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content.decode("UTF-8"))
        self.assertFalse(j['success'])

    def test_login_bad_password_failed(self):
        try:
            coreLogin(username='existinguser', password='pppp')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_url_login_bad_password_failed(self):
        args = {
            'username': 'existinguser',
            'password': 'pppp'
        }
        response = self.client.post('/accounts/login', args)
        self.assertEqual(response.status_code, 200)

    def test_ajaxurl_login_bad_password_failed(self):
        args = {
            'username': 'existinguser',
            'password': 'pppp'
        }
        response = self.client.post(
            '/accounts/login',
            args,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content.decode("UTF-8"))
        self.assertFalse(j['success'])

    def test_login_success(self):
        myuser = coreLogin(username='existinguser', password='fubar')
        self.assertIsNotNone(myuser)

    def test_url_login_success(self):
        args = {
            'username': 'existinguser',
            'password': 'fubar'
        }
        response = self.client.post('/accounts/login', args)
        # Rdirect to / when login in succeded
        self.assertEqual(response.status_code, 302)

    def test_ajaxurl_login_success(self):
        args = {
            'username': 'existinguser',
            'password': 'fubar'
        }
        response = self.client.post(
            '/accounts/login',
            args,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content.decode("UTF-8"))
        self.assertTrue(j['success'])
