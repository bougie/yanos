from sqlalchemy import exc

from ... import db
from ..models import Priority

def corePriorityAdd(name):
	try:
		pri = Priority(name=name)

		db.session.add(pri)
		db.session.commit()
	except exc.IntegrityError as e:
		raise Exception('Priority is already in use')
	except:
		raise Exception('unknown error')

def corePriorityDelete(id):
	try:
		pri = Priority.query.filter_by(id=int(id)).first()

		db.session.delete(pri)
		db.session.commit()
	except Exception as e:
		raise Exception('unknown error')

def corePriorityEdit(id, name):
	try:
		pri = Priority.query.filter_by(id=int(id)).first()

		pri.name = name

		db.session.commit()
	except exc.IntegrityError as e:
		raise Exception('Priority is already in use')
	except Exception as e:
		raise Exception('unknown error')


def corePriorityList():
	priList = []
	
	for item in Priority.query.all():
		priList.append({'id': item.id, 'name': item.name})

	return priList
