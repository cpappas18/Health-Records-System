from unittest import TestCase
from src.command import *


class TestInvoker(TestCase):

    def setUp(self):
        self.invoker = Invoker()

    def test_register(self):
        command = ICommand()
        self.invoker.register(command)
        self.assertEqual(self.invoker._commands, [command])

    def test_execute(self):
        self.fail()

    def test_undo(self):
        self.fail()

    def test_redo(self):
        self.fail()


class TestAddPatientCommand(TestCase):
    def test_execute(self):
        self.fail()

    def test_undo(self):
        self.fail()


class TestRemovePatientCommand(TestCase):
    def test_execute(self):
        self.fail()

    def test_undo(self):
        self.fail()


class TestAddMedicationCommand(TestCase):
    def test_execute(self):
        self.fail()

    def test_undo(self):
        self.fail()


class TestRemoveMedicationCommand(TestCase):
    def test_execute(self):
        self.fail()

    def test_undo(self):
        self.fail()


class TestAddTestResultsCommand(TestCase):
    def test_execute(self):
        self.fail()

    def test_undo(self):
        self.fail()
