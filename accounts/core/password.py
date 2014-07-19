from django.contrib.auth.models import User

from lib.exception import CoreException


def corePassword(username, old_password, password, password2):
    if password != password2:
        raise CoreException(1, 'passwords have to be equals')

    try:
        user = User.objects.get(username=username)

        user.set_password(password)
        user.save()
    except Exception as e:
        print(str(e))
        raise CoreException(0, 'unknown error')
