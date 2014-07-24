from django.test import TestCase
from django.contrib.auth.models import User

from .models import Priority, State
from lib.exception import CoreException
from .core.priority import corePriorityAdd, corePriorityDelete, \
    corePriorityEdit, corePriorityList
from .core.state import coreStateAdd, coreStateDelete, coreStateEdit, \
    coreStateList


class PriorityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='myuser',
            password='fubar')
        self.user2 = User.objects.create_user(
            username='myuser2',
            password='fubar2')
        Priority(name='existing_priority', user=self.user).save()
        Priority(name='existing_priority2', user=self.user2).save()

    def test_creating_success(self):
        corePriorityAdd('test', user=self.user)
        self.assertEqual(3, Priority.objects.all().count())

        corePriorityAdd('test2', user=self.user2)
        self.assertEqual(4, Priority.objects.all().count())

    def test_creating_existing_name(self):
        try:
            # Priority exists for user
            corePriorityAdd('existing_priority', user=self.user)
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_creating_existing_name_with_another_user(self):
        # This priority does not exists for the user 2
        corePriorityAdd('existing_priority', user=self.user2)

    def test_deleting_success(self):
        corePriorityDelete(1, user=self.user)

    def test_deleting_of_another_user(self):
        try:
            # Priority 2 is not own by user
            corePriorityDelete(2, user=self.user)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_deleting_non_existing(self):
        try:
            corePriorityDelete(1337, user=self.user)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_success(self):
        corePriorityEdit(1, 'newname', user=self.user)

        pri = Priority.objects.get(name='newname')
        self.assertIsNotNone(pri)

    def test_editing_of_another_user(self):
        try:
            corePriorityEdit(2, 'newname', user=self.user)
        except CoreException as e:
            self.assertEqual(0, e.code)

        try:
            pri = Priority.objects.get(name='newname', user=self.user)
        except:
            pri = None
        self.assertIsNone(pri)

    def test_editing_non_existing(self):
        try:
            corePriorityEdit(1337, 'fubarland', user=self.user)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_existing_name(self):
        try:
            corePriorityEdit(1, 'existing_priority', user=self.user)
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_listing(self):
        priorities = corePriorityList(user=self.user)
        self.assertEqual(1, len(priorities))
        self.assertEqual(priorities[0]['name'], 'existing_priority')


class StateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='myuser',
            password='fubar')
        self.user2 = User.objects.create_user(
            username='myuser2',
            password='fubar2')
        State(name='existing_state', user=self.user).save()
        State(name='existing_state2', user=self.user2).save()

    def test_creating_success(self):
        coreStateAdd('test', user=self.user)
        self.assertEqual(3, State.objects.all().count())

        coreStateAdd('test', user=self.user2)
        self.assertEqual(4, State.objects.all().count())

    def test_creating_existing_name(self):
        try:
            coreStateAdd('existing_state', user=self.user)
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_creating_existing_name_with_another_user(self):
        # This state does not exist for user2
        coreStateAdd('existing_state', user=self.user2)

    def test_deleting_success(self):
        coreStateDelete(1, user=self.user)

    def test_deleting_of_another_user(self):
        try:
            # State 2 is not own by user
            coreStateDelete(2, user=self.user)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_deleting_non_existing(self):
        try:
            coreStateDelete(1337, user=self.user)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_success(self):
        coreStateEdit(1, 'newname', user=self.user)

        st = State.objects.get(name='newname', user=self.user)
        self.assertIsNotNone(st)

    def test_editing_of_another_user(self):
        try:
            coreStateEdit(1, 'newname', user=self.user2)
        except CoreException as e:
            self.assertEqual(0, e.code)

        try:
            st = State.objects.get(name='newname', user=self.user2)
        except:
            st = None
        self.assertIsNone(st)

    def test_editing_non_existing(self):
        try:
            coreStateEdit(1337, 'fubarland', user=self.user)
        except CoreException as e:
            self.assertEqual(0, e.code)

    def test_editing_existing_name(self):
        try:
            coreStateEdit(1, 'existing_state', user=self.user)
        except CoreException as e:
            self.assertEqual(1, e.code)

    def test_listing(self):
        states = coreStateList(user=self.user)
        self.assertEqual(1, len(states))
        self.assertEqual(states[0]['name'], 'existing_state')
