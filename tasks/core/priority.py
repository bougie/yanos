from django.db import IntegrityError

from tasks.models import Priority
from lib.exception import CoreException


def corePriorityAdd(name):
    try:
        pri = Priority()
        pri.name = name

        pri.save()
    except IntegrityError:
        raise CoreException(1, 'Priority name is already in use')
    except:
        raise CoreException(0, 'unknown error')


def corePriorityDelete(id):
    try:
        Priority.objects.get(id=int(id)).delete()
    except Exception:
        raise CoreException(0, 'unknown error')


def corePriorityEdit(id, name):
    try:
        pri = Priority.objects.get(id=int(id))

        pri.name = name

        pri.save()
    except django.db.IntegrityError:
        raise CoreException(1, 'Priority name is already in use')
    except Exception:
        raise CoreException(0, 'unknown error')


def corePriorityList():
    priList = []

    for item in Priority.objects.all():
        priList.append({'id': item.id, 'name': item.name})

    return priList
