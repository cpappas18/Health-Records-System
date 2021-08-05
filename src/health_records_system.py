import copy


class HealthRecordsSystem(object):
    """
    Implements an Electronic Health Records System that stores patient information.
    Adheres to the Singleton Design Pattern such that only one instantiation of this class is possible.
    Assumes the role of Receiver as part of the Command Design Pattern.
    """

    __instance = None

    @staticmethod
    def get_instance():
        """
        Static access method for Singleton object
        """
        if HealthRecordsSystem.__instance is None:
            HealthRecordsSystem()
        return HealthRecordsSystem.__instance

    def __init__(self):
        if HealthRecordsSystem.__instance is None:
            HealthRecordsSystem.__instance = self
            self._patients = {}  # stores patients in a dictionary of ID:patient pairs
        else:
            raise Exception("HealthRecordsSystem class is a Singleton.")

    @staticmethod
    def _reset():
        """
        Removes Singleton instance to allow for a new instantiation
        """
        HealthRecordsSystem.__instance = None

    def get_patient(self, id):
        """
        Retrieves patient by their ID number.
        :param id: unique number given to patient upon creation
        :return: patient corresponding to the ID if it exists in the system, otherwise returns None
        """
        try:
            return self._patients[id]
        except KeyError:
            print(f"Patient #{id} does not exist in the System.")
            return None

    def add_patient(self, patient):
        """
        Adds a patient to the system if the ID does not already exist.
        If it does exist, the patient's information will be overwritten upon the user's input of Y/N.
        :param patient: the new patient to be added to the system
        """
        if patient.id in self._patients:
            overwrite = input(f"Patient #{patient.id} already exists. Overwrite? Y/N")
            if overwrite == "Y":
                self._patients[patient.id] = patient
                print(f"Patient #{patient.id} successfully added to the system.")
            else:
                print(f"Failure: Patient #{patient.id} was not added to the system.")
        else:
            self._patients[patient.id] = patient
            print(f"Patient #{patient.id} successfully added to the system.")
        
    def remove_patient(self, id):
        """
        Removes a patient from the system if the ID number exists, otherwise does nothing.
        :param id: ID number of the patient to remove
        :return: the removed patient if removal is successful, otherwise returns None
        """
        try:
            patient = self._patients[id]
            del self._patients[id]
            print(f"Patient #{id} successfully removed from the system.")
            return patient
        except KeyError:
            print(f"Patient #{id} does not exist in the system.")
            return None


class Patient(object):

    def __init__(self, id, name, age, phone_number):
        self._id = id
        self._name = name
        self._age = age
        self._phone_number = phone_number
        self._medication = {}
        self._test_results = {}

    @property
    def id(self):
        return self._id

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def medication(self):
        return self._medication

    @property
    def test_results(self):
        return self._test_results

    def get_medication(self, med_name):
        """
        Retrieves a patient's medication by its name.
        :param med_name: name of the medication
        :return: medication corresponding to the name if it exists in the patient's record, otherwise returns None
        """
        try:
            return self._medication[med_name]
        except KeyError:
            print(f"{med_name} does not exist in the patient's record.")
            return None
    
    def add_medication(self, med):
        """
        Adds a medication to the patient's record if the medication's name does not already exist.
        If it does exist, the medication's information will be overwritten upon the user's input of Y/N.
        :param med: the new medication to be added to the patient's record
        """

        if med.name in self._medication:
            overwrite = input(f"Patient #{self._id} is already taking this medication. Overwrite dosage and frequency? Y/N")
            if overwrite == "Y":
                self._medication[med.name] = med  # update the medication information
                print(f"Medication successfully updated in patient #{self._id}'s record.")
            else:
                print(f"Failure: Medication was not updated in patient #{self._id}'s record.")
        else:
            self._medication[med.name] = med
            print(f"Medication successfully added to patient #{self._id}'s record.")

    def remove_medication(self, med_name):
        """
        Removes a medication from the patient's record if the name exists, otherwise does nothing.
        :param med_name: name of the medication to remove
        :return: the removed medication if removal is successful, otherwise returns None
        """
        try:
            med = self._medication[med_name]
            del self._medication[med_name]
            print(f"{med_name} successfully removed from the patient's record.")
            return med
        except KeyError:
            print(f"{med_name} does not exist in the patient's record.")
            return None

    def clear_medication(self):
        """
        Clears all medication from the patient's record.
        """
        self._medication.clear()

    def get_test_results(self, name, date):
        """
        Retrieves a patient's test results by its name and date.
        :param name: name of the test
        :param date: date that the test was performed (DD/MM/YYYY)
        :return: test results corresponding to the name and date if it exists in the patient's record, otherwise returns None
        """
        try:
            return self._test_results[(name, date)]
        except KeyError:
            print(f"Test for {name} does not exist in the patient's record on {date}.")
            return None

    def add_test_results(self, name, date, result):
        """
        Adds a test result to the patient's record if the test's name does not already exist on the specified date.
        If it does exist, the test result will be overwritten upon the user's input of Y/N.
        :param name: name of the test
        :param date: date that the test was performed (DD/MM/YYYY)
        :param result: result of the test
        """
        if (name, date) in self._test_results.keys():
            overwrite = input(f"A result for this test on {date} has already been recorded. Overwrite test result? Y/N")
            if overwrite == "Y":
                self._test_results[(name, date)] = result
                print(f"Test result successfully updated in patient #{self._id}'s record.")
            else:
                print(f"Failure: Test result was not updated in patient #{self._id}'s record.")
                return
        else:
            self._test_results[(name, date)] = result
            print(f"Test result successfully added to patient #{self._id}'s record.")

    def clear_test_results(self):
        """
        Clears all tests from the patient's record.
        """
        self._test_results.clear()


class Medication(object):

    def __init__(self, name, dosage, frequency):
        self._name = name
        self._dosage = dosage
        self._frequency = frequency

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def dosage(self):
        return self._dosage

    @dosage.setter
    def dosage(self, value):
        self._dosage = value

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        self._frequency = value
