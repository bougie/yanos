from yanos import db

print("Creating database...")

from yanos.accounts.models import *
from yanos.tasks.models import *
db.create_all()
db.session.commit()
