from django.test import TestCase

from .models import Priority, State
from lib.exception import CoreException
from .core.priority import corePriorityAdd, corePriorityDelete, \
    corePriorityEdit, corePriorityList
from .core.state import coreStateAdd, coreStateDelete, coreStateEdit, \
    coreStateList


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


class StateTestCase(TestCase):
    def setUp(self):
        State(name='existing_state').save()

    def test_creating_success(self):
        coreStateAdd('test')
        self.assertEqual(2, State.objects.all().count())

    def test_creating_existing_name(self):
        try:
            coreStateAdd('existing_state')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_deleting_success(self):
        coreStateDelete(1)

    def test_deleting_non_existing(self):
        try:
            coreStateDelete(1337)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_success(self):
        coreStateEdit(1, 'newname')

        st = State.objects.get(name='newname')
        self.assertIsNotNone(st)

    def test_editing_non_existing(self):
        try:
            coreStateEdit(1337, 'fubarland')
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_existing_name(self):
        try:
            coreStateEdit(1, 'existing_state')
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_listing(self):
        states = coreStateList()
        self.assertEqual(1, len(states))
        self.assertEqual(states[0]['name'], 'existing_state')
