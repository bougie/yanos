from django.db import IntegrityError

from tasks.models import State
from lib.exception import CoreException


def coreStateAdd(name, user):
    try:
        st = State()
        st.name = name
        st.user = user

        st.save()
    except IntegrityError:
        raise CoreException(1, 'State name is already in use')
    except:
        raise CoreException(0, 'unknown error')


def coreStateDelete(id, user):
    try:
        State.objects.get(id=int(id)).delete()
    except Exception:
        raise CoreException(0, 'unknown error')


def coreStateEdit(id, name, user):
    try:
        st = State.objects.get(id=int(id), user=user)

        st.name = name

        st.save()
    except IntegrityError:
        raise CoreException(1, 'State name is already in use')
    except Exception:
        raise CoreException(0, 'unknown error')


def coreStateList(user):
    stList = []

    for item in State.objects.all().filter(user=user):
        stList.append({'id': item.id, 'name': item.name})

    return stList
