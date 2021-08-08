from abc import ABCMeta, abstractmethod
import copy
import sys

class ICommand(metaclass=ABCMeta):
    """
    Defines the command interface as part of the Command Design Pattern
    """

    @staticmethod
    @abstractmethod
    def execute(*args):
        """ Execution of the command """

    @staticmethod
    @abstractmethod
    def undo(*args):
        """ Undo the command """


class Invoker(metaclass=ABCMeta):
    """
    Passes requests to the Health Records System by executing commands
    """

    def __init__(self):
        self._commands = []
        self._history = []
        self._position = -1  # position in command history

    @property
    def history(self):
        return self._history

    def register(self, command):
        """
        Adds a command to the list of recognized commands
        :param command: the command to add
        """
        self._commands.append(command)

    def execute(self, command, *args):
        """
        Executes the command and adds it to the command history
        :param command: a subtype of the ICommand interface, the command to be executed
        :param args: any additional arguments that the Receiver (the Health Records System) requires to execute the command
        """
        if command in self._commands:
            self._position += 1
            command.execute(*args)

            if len(self._history) == self._position:  # nothing has been undone or all undone commands have been redone
                self._history.append((command, args))

            else:  # some commands have been undone before this command was executed
                self._history = self._history[:self._position]  # erase history that occurs after the current position
                self._history.append((command, args))

        else:
            print(f"You must register command {command} before executing it.")

    def undo(self):
        """
        Undoes the last performed action based on the current position in the command history.
        If all actions have already been undone, there are no effects.
        """
        if self._position > -1:
            command_to_undo = self._history[self._position]  # (command, args)
            command_to_undo[0].undo(*command_to_undo[1])
            self._position -= 1
            print("The last action has been undone.")
        else:
            print("No commands have been performed yet or all commands have already been undone.")

    def redo(self):
        """
        Redoes the last undone command if the current position is not at the end of the command history, meaning some
        commands have been undone previously.
        Otherwise, if the current position is at the end of the command history, the last performed command is performed
        again.
        If no commands have been performed yet, there are no effects.
        """
        if self._position == -1:  # no commands have been performed
            print("There are no commands to redo.")

        elif self._position < len(self._history)-1:  # redo the last undone command
            self._position += 1
            command_to_redo = self._history[self._position]  # (command, args)
            command_to_redo[0].execute(*command_to_redo[1])
            print("The last action has been redone.")

        else:  # redo the last performed action
            command_to_redo = self._history[self._position]  # (command, args)
            command_to_redo[0].execute(*command_to_redo[1])
            print("The last action has been redone.")


class AddPatientCommand(ICommand):

    def __init__(self, system):
        self._system = system

    def execute(self, *args):
        """
        Adds a patient to the system
        :param args: requires one argument; the Patient object to be added
        """
        patient = args[0]
        self._system.add_patient(patient)

    def undo(self, *args):
        """
        Undoes the action by removing the patient from the system
        :param args: requires one argument; the Patient object to be removed
        """
        patient = args[0]
        self._system.remove_patient(patient.id)


class RemovePatientCommand(ICommand):

    def __init__(self, system):
        self._system = system

    def execute(self, *args):
        """
        Removes a patient from the system
        :param args: requires one argument; the Patient object to be removed
        """
        self._system.remove_patient(args[0].id)

    def undo(self, *args):
        """
        Undoes the action by adding the patient back to the system
        :param args: requires one argument; the Patient object to be added
        """
        self._system.add_patient(args[0])


class AddMedicationCommand(ICommand):

    def __init__(self, system):
        self._system = system
        self._orig_medication = {}  # stores the previous state of the patient's medication record

    def execute(self, *args):
        """
        Adds a medication to a patient's record
        :param args: requires two arguments; the Patient object and the Medication object to be added
        """
        self._orig_medication = copy.deepcopy(args[0].medication)  # store the previous medication in case it needs to be recovered later
        args[0].add_medication(args[1])

    def undo(self, *args):
        """
        Undoes the last addition to the patient's medication record by recovering the previous state of the medication
        :param args: requires one argument; the Patient object
        """
        patient = args[0]
        patient.clear_medication()

        # suppress console output from add_medication function
        save_stdout = sys.stdout
        sys.stdout = open('trash', 'w')

        for med in self._orig_medication.values():
            patient.add_medication(med)

        sys.stdout = save_stdout  # restore console output


class RemoveMedicationCommand(ICommand):

    def __init__(self, system):
        self._system = system

    def execute(self, *args):
        """
        Removes a medication from a patient's record
        :param args: requires two arguments; the Patient object and the Medication object to be removed
        """
        args[0].remove_medication(args[1].name)

    def undo(self, *args):
        """
        Undoes the removal of a medication by adding it back to a patient's record
        :param args: requires two arguments; the Patient object and the Medication object to be added back
        """
        args[0].add_medication(args[1])


class AddTestResultsCommand(ICommand):

    def __init__(self, system):
        self._system = system
        self._orig_test_results = {}  # stores the previous state of the patient's test results record

    def execute(self, *args):
        """
        Adds test results to a patient's record
        :param args: requires four arguments; the Patient object, the name of the test, the date it was performed (DD/MM/YYYY), and the test result
        """
        self._orig_test_results = copy.deepcopy(args[0].test_results)  # store the previous test results in case they need to be recovered later
        args[0].add_test_results(args[1], args[2], args[3])

    def undo(self, *args):
        """
        Undoes the last addition to the patient's test results record by recovering the previous state of the test results
        :param args: requires one argument; the Patient object
        """
        patient = args[0]
        patient.clear_test_results()

        # suppress console output from add_test_results function
        save_stdout = sys.stdout
        sys.stdout = open('trash', 'w')

        for (name, date), result in self._orig_test_results.items():
            patient.add_test_results(name, date, result)

        sys.stdout = save_stdout  # restore console output
