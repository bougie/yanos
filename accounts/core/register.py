from django.contrib.auth.models import User

from lib.exception import CoreException


def coreRegister(username, password, password2):
    if password != password2:
        raise CoreException(1, 'passwords have to be equals')

    if User.objects.filter(username=username).exists():
        raise CoreException(2, 'Username alrady in use')

    try:
        User.objects.create_user(username=username, password=password)
    except:
        raise CoreException(0, 'unknown error')
