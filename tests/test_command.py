from unittest import TestCase
from unittest.mock import Mock
from src.command import *


class TestInvoker(TestCase):

    def setUp(self):
        self.invoker = Invoker()

    def test_register(self):
        command_stub = Mock(ICommand)
        self.invoker.register(command_stub)
        self.assertEqual(self.invoker._commands, [command_stub])

    def test_execute_for_none_undone(self):
        command_stub = Mock(ICommand)
        self.invoker.register(command_stub)
        self.invoker.execute(command_stub, "arg")
        self.assertEqual(self.invoker._history, [(command_stub, ("arg",))])

    def test_execute_for_some_undone(self):
        command_stub1 = Mock(ICommand)
        command_stub2 = Mock(ICommand)
        self.invoker.register(command_stub1)
        self.invoker.register(command_stub2)
        self.invoker.execute(command_stub1, "command_1_first")
        self.invoker.execute(command_stub1, "command_1_second")
        self.invoker.undo()
        self.invoker.execute(command_stub2, "command_2_first")
        self.assertEqual(self.invoker._history, [(command_stub1, ("command_1_first",)), (command_stub2, ("command_2_first",))])

    def test_execute_for_command_not_registered(self):
        command_stub = Mock(ICommand)
        self.invoker.execute(command_stub, "arg")
        self.assertEqual(self.invoker._history, [])

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
