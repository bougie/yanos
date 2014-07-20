from django.test import TestCase

from .models import Priority
from lib.exception import CoreException
from .core.priority import corePriorityAdd, corePriorityDelete, \
    corePriorityEdit, corePriorityList


class PriorityTestCase(TestCase):
    def setUp(self):
        Priority(name='existing_priority').save()

    def test_creating_success(self):
        corePriorityAdd('test')
        self.assertEqual(2, Priority.objects.all().count())

    def test_creating_existing_name(self):
        try:
            corePriorityAdd('existing_priority')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_deleting_success(self):
        corePriorityDelete(1)

    def test_deleting_non_existing(self):
        try:
            corePriorityDelete(1337)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_success(self):
        corePriorityEdit(1, 'newname')

        pri = Priority.objects.get(name='newname')
        self.assertIsNotNone(pri)

    def test_editing_non_existing(self):
        try:
            corePriorityEdit(1337, 'fubarland')
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_existing_name(self):
        try:
            corePriorityEdit(1, 'existing_priority')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_listing(self):
        priorities = corePriorityList()
        self.assertEqual(1, len(priorities))
        self.assertEqual(priorities[0]['name'], 'existing_priority')
