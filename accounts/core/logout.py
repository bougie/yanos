from django.contrib.auth import logout


def coreLogout(request):
    try:
        logout(request)
    except Exception as e:
        print(str(e))
