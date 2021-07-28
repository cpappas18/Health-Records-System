from abc import ABCMeta, abstractmethod


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
        
        :param command:
        :param args:
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
        if self._position > -1:
            command_to_undo = self._history[self._position]  # (command, args)
            command_to_undo[0].undo(command_to_undo[1])
            self._position -= 1
            print("The last action has been undone.")
        else:
            print(f"All actions have been undone.")

    def redo(self):
        if self._position < len(self._history)-1:  # redo the last undone command
            self._position += 1
            command_to_redo = self._history[self._position]  # (command, args)
            command_to_redo[0].execute(command_to_redo[1])

        else:  # redo the last performed action
            command_to_redo = self._history[self._position]  # (command, args)
            command_to_redo[0].execute(command_to_redo[1])

        print("The last action has been redone.")


class AddPatientCommand(ICommand):

    def __init__(self, system):
        self._system = system

    def execute(self, *args):
        patient = args[0]
        self._system.add_patient(patient)

    def undo(self, *args):
        patient = args[0]
        self._system.remove_patient(patient.id)


class RemovePatientCommand(ICommand):

    def __init__(self, system):
        self._system = system

    def execute(self, *args):
        self._system.remove_patient(args[0].id)

    def undo(self, *args):
        self._system.add_patient(args[0])


class AddMedicationCommand(ICommand):

    def __init__(self, system):
        self._system = system

    def execute(self, *args):
        args[0].add_medication(args[1])

    def undo(self, *args):
        args[0].remove_medication(args[1])


class RemoveMedicationCommand(ICommand):

    def __init__(self, system):
        self._system = system

    def execute(self, *args):
        args[0].remove_medication(args[1])

    def undo(self, *args):
        args[0].add_medication(args[1])


class AddTestResultsCommand(ICommand):

    def __init__(self, system):
        self._system = system
        self._orig_test_results = {}

    def execute(self, *args):
        self._orig_test_results = args[0].test_results
        args[0].add_test_results(args[1], args[2], args[3])

    def undo(self, *args):
        patient = args[0]
        patient.clear_test_results()

        for (name, date), result in self._orig_test_results.items():
            patient.add_test_results(name, date, result)
