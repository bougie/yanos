from django.db import IntegrityError

from tasks.models import Priority
from lib.exception import CoreException


def corePriorityAdd(name, user):
    try:
        pri = Priority()
        pri.name = name
        pri.user = user

        pri.save()
    except IntegrityError:
        raise CoreException(1, 'Priority name is already in use')
    except:
        raise CoreException(0, 'unknown error')


def corePriorityDelete(id, user):
    try:
        Priority.objects.get(id=int(id), user=user).delete()
    except Exception:
        raise CoreException(0, 'unknown error')


def corePriorityEdit(id, name, user):
    try:
        pri = Priority.objects.get(id=int(id), user=user)

        pri.name = name

        pri.save()
    except IntegrityError:
        raise CoreException(1, 'Priority name is already in use')
    except Exception:
        raise CoreException(0, 'unknown error')


def corePriorityList(user):
    priList = []

    for item in Priority.objects.all().filter(user=user):
        priList.append({'id': item.id, 'name': item.name})

    return priList
