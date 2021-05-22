from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def execute(*args):
        """ Execution of command """


class IUndoRedo(metaclass=ABCMeta):
    """ Undo/Redo Interface """

    @staticmethod
    @abstractmethod
    def history():
        """ returns the history of states """

    @staticmethod
    @abstractmethod
    def undo():
        """ undoes the history of states """

    @staticmethod
    @abstractmethod
    def redo():
        """ redoes the history of states """


# TODO change class name
class Invoker(IUndoRedo):
    """ Invoker class """

    def __init__(self):
        self._commands = {}
        self._history = []
        self._position = -1

    @property
    def history(self):
        return self._history

    def register(self, name, command):
        self._commands[name] = command

    def execute(self):
        #TODO implement

    def undo(self):
        if self._position > 0:
            self._position -= 1
        # TODO implement

    def redo(self):
        #TODO implement

class AddPatientCommand(ICommand):
    #TODO implement

class RemovePatientCommand(ICommand):
    #TODO implement

class AddMedicationCommand(ICommand):
    #TODO implement

class RemoveMedicationCommand(ICommand):
    #TODO implement

class AddTestResults(ICommand):
    #TODO implement