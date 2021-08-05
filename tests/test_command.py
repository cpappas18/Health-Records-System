from unittest import TestCase
from unittest.mock import Mock
from src.command import *
from src.health_records_system import *
import mock
import builtins


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

    def test_undo_for_history_non_empty(self):
        class MockCommand(ICommand):
            def __init__(self):
                self.executed = False
                self.undone = False

            def execute(self, *args):
                self.executed = True

            def undo(self, *args):
                self.undone = True

        command_stub = MockCommand()
        self.invoker.register(command_stub)
        self.invoker.execute(command_stub, "arg")
        prev_position = self.invoker._position
        self.invoker.undo()
        self.assertEqual(command_stub.undone, True)
        self.assertEqual(self.invoker._position, prev_position-1)

    def test_undo_for_history_empty(self):
        class MockCommand(ICommand):
            def __init__(self):
                self.executed = False
                self.undone = False

            def execute(self, *args):
                self.executed = True

            def undo(self, *args):
                self.undone = True

        command_stub = MockCommand()
        self.invoker.register(command_stub)
        prev_position = self.invoker._position
        self.invoker.undo()
        self.assertEqual(command_stub.undone, False)
        self.assertEqual(self.invoker._position, prev_position)

    def test_redo_for_commands_previously_undone(self):
        class MockCommand(ICommand):
            def __init__(self):
                self.executed = False
                self.undone = False
                self.redone = False
                self.count = 0

            def execute(self, *args):
                self.executed = True
                self.count += 1
                if self.count > 1:
                    self.redone = True

            def undo(self, *args):
                self.undone = True

        command_stub = MockCommand()
        self.invoker.register(command_stub)
        self.invoker.execute(command_stub, "arg")
        self.invoker.undo()
        prev_position = self.invoker._position
        self.invoker.redo()
        self.assertEqual(command_stub.redone, True)
        self.assertEqual(self.invoker._position, prev_position+1)

    def test_redo_for_last_command_not_undone(self):
        class MockCommand(ICommand):
            def __init__(self):
                self.executed = False
                self.undone = False
                self.redone = False
                self.count = 0

            def execute(self, *args):
                self.executed = True
                self.count += 1
                if self.count > 1:
                    self.redone = True

            def undo(self, *args):
                self.undone = True

        command_stub = MockCommand()
        self.invoker.register(command_stub)
        self.invoker.execute(command_stub, "arg")
        prev_position = self.invoker._position
        self.invoker.redo()
        self.assertEqual(command_stub.redone, True)
        self.assertEqual(self.invoker._position, prev_position)


class TestAddPatientCommand(TestCase):

    def setUp(self):
        self.system = HealthRecordsSystem()
        self.command = AddPatientCommand(self.system)

    def tearDown(self):
        HealthRecordsSystem._reset()

    def test_execute(self):
        patient = Patient(1, "Jane", 20, 123)
        self.command.execute(patient)
        self.assertEqual(self.system._patients, {1: patient})

    def test_undo(self):
        patient = Patient(1, "Jane", 20, 123)
        self.command.execute(patient)
        self.command.undo(patient)
        self.assertEqual(self.system._patients, {})


class TestRemovePatientCommand(TestCase):

    def setUp(self):
        self.system = HealthRecordsSystem()
        self.command = RemovePatientCommand(self.system)

    def tearDown(self):
        HealthRecordsSystem._reset()

    def test_execute(self):
        patient = Patient(1, "Jane", 20, 123)
        AddPatientCommand(self.system).execute(patient)  # adds the patient
        self.command.execute(patient)  # removes the patient
        self.assertEqual(self.system._patients, {})

    def test_undo(self):
        patient = Patient(1, "Jane", 20, 123)
        AddPatientCommand(self.system).execute(patient)  # adds the patient
        self.command.execute(patient)  # removes the patient
        self.command.undo(patient)  # adds the patient again
        self.assertEqual(self.system._patients, {1: patient})


class TestAddMedicationCommand(TestCase):

    def setUp(self):
        self.system = HealthRecordsSystem()
        self.command = AddMedicationCommand(self.system)

    def tearDown(self):
        HealthRecordsSystem._reset()

    def test_execute(self):
        patient = Patient(1, "Jane", 20, 123)
        med = Medication("Advil", "1 tablet", "once a day")
        self.command.execute(patient, med)
        self.assertEqual(patient._medication, {"Advil": med})

    def test_undo(self):
        patient = Patient(1, "Jane", 20, 123)
        med1 = Medication("Advil", "1 tablet", "once a day")
        self.command.execute(patient, med1)
        med2 = Medication("Advil", "2 tablet", "once a day")

        with mock.patch.object(builtins, 'input', lambda _: 'Y'):
            self.command.execute(patient, med2)
            self.command.undo(patient)
            cur_med = patient.get_medication("Advil")
            self.assertEqual(cur_med.dosage, "1 tablet")


class TestRemoveMedicationCommand(TestCase):

    def setUp(self):
        self.system = HealthRecordsSystem()
        self.command = RemoveMedicationCommand(self.system)

    def tearDown(self):
        HealthRecordsSystem._reset()

    def test_execute(self):
        patient = Patient(1, "Jane", 20, 123)
        med = Medication("Advil", "1 tablet", "once a day")
        AddMedicationCommand(self.system).execute(patient, med)  # add medication
        self.command.execute(patient, med)  # remove medication
        self.assertEqual(patient._medication, {})

    def test_undo(self):
        patient = Patient(1, "Jane", 20, 123)
        med = Medication("Advil", "1 tablet", "once a day")
        AddMedicationCommand(self.system).execute(patient, med)  # add medication
        self.command.execute(patient, med)  # remove medication
        self.command.undo(patient, med)  # add medication again
        self.assertEqual(patient._medication, {"Advil": med})


class TestAddTestResultsCommand(TestCase):

    def setUp(self):
        self.system = HealthRecordsSystem()
        self.command = AddTestResultsCommand(self.system)

    def tearDown(self):
        HealthRecordsSystem._reset()

    def test_execute(self):
        patient = Patient(1, "Jane", 20, 123)
        self.command.execute(patient, "COVID", "June 26, 2021", "Negative")
        self.assertEqual(patient.test_results, {("COVID", "June 26, 2021"): "Negative"})

    def test_undo(self):
        patient = Patient(1, "Jane", 20, 123)
        self.command.execute(patient, "COVID", "June 26, 2021", "Negative")

        with mock.patch.object(builtins, 'input', lambda _: 'Y'):
            self.command.execute(patient, "COVID", "June 26, 2021", "Positive")
            self.command.undo(patient)
            self.assertEqual(patient.test_results, {("COVID", "June 26, 2021"): "Negative"})

