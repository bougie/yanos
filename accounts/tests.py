from django.test import TestCase
from django.contrib.auth.models import User

from lib.exception import CoreException
from .core.register import coreRegister
from .core.login import coreLogin


class AccountsTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='existinguser', password='fubar')

    def test_registering_bad_password(self):
        try:
            coreRegister('username', 'p1', 'p0')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_registering_existing_username(self):
        try:
            coreRegister('existinguser', 'p1', 'p1')
        except CoreException as e:
            self.assertEqual(2, e.code)

    def test_registering_success(self):
        coreRegister('pwet', 'camembert', 'camembert')

        self.assertEqual(2, User.objects.all().count())

    def test_login_bad_username(self):
        try:
            coreLogin(username='unexistinguser', password='pwet')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_login_bad_password(self):
        try:
            coreLogin(username='existinguser', password='pppp')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_login_success(self):
        myuser = coreLogin(username='existinguser', password='fubar')
        self.assertIsNotNone(myuser)
