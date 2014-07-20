from django.contrib.auth import authenticate

from lib.exception import CoreException


def coreLogin(username, password, remember_me=False):
    try:
        user = authenticate(username=username, password=password)
    except Exception as e:
        print(str(e))
        raise CoreException(0, 'unknown error')
    else:
        if user is None or not user.is_active:
            raise CoreException(1, 'User is not active')

        return user

    return None
