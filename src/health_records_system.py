class HealthRecordsSystem(object):

    __instance = None

    @staticmethod
    def get_instance():
        if HealthRecordsSystem.__instance is None:
            HealthRecordsSystem()
        return HealthRecordsSystem.__instance

    def __init__(self):
        if HealthRecordsSystem.__instance is None:
            HealthRecordsSystem.__instance = self
            self.__patients = {}
        else:
            raise Exception("HealthRecordsSystem class is a Singleton.")

    def get_patient(self, id):
        return self.__patients[id]

    def add_patient(self, patient):
        if patient.id in self.__patients:
            overwrite = input(f"Patient #{patient.id} already exists. Overwrite? Y/N")
            if overwrite == "Y":
                self.__patients[patient.id] = patient
                print(f"Patient #{patient.id} successfully added to the system.")
            else:
                print(f"Failure: Patient #{patient.id} was not added to the system.")
                return
        else:
            self.__patients[patient.id] = patient
            print(f"Patient #{patient.id} successfully added to the system.")
        
    def remove_patient(self, id):
        try:
            del self.__patients[id]
            print(f"Patient #{id} successfully removed from the system.")
        except KeyError:
            print(f"Patient #{id} does not exist in the system.")
            return
        
    def print_patients(self):
        for (name, info) in self.__patients.items():
            print(f"Patient: {name}, Information: {info}")


class Patient(object):

    def __init__(self, id, name, age, phone_number):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__phone_number = phone_number
        self.__medication = {}
        self.__test_results = {}

    @property
    def id(self):
        return self.__id

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def medication(self):
        return self.__medication

    @property
    def test_results(self):
        return self.__test_results
    
    def add_medication(self, med):
        if med.name in self.__medication:
            overwrite = input(f"Patient #{self.__id} is already taking this medication. Overwrite dosage and frequency? Y/N")
            if overwrite == "Y":
                self.__medication[med.name] = med
                print(f"Medication successfully updated in patient #{self.__id}'s record.")
            else:
                print(f"Failure: Medication was not updated in patient #{self.__id}'s record.")
                return
        else:
            self.__medication[med.name] = med
            print(f"Medication successfully added to patient #{self.__id}'s record.")

    # TODO specify precondition
    def remove_medication(self, med):
        del self.__medication[med.name]
        print(f"Medication successfully removed from patient #{self.__id}'s record.")

    def add_test_results(self, name, date, result):
        if (name, date) in self.__test_results.keys():
            overwrite = input(f"A result for this test on {date} has already been recorded. Overwrite test result? Y/N")
            if overwrite == "Y":
                self.__test_results[(name, date)] = result
                print(f"Test result successfully updated in patient #{self.__id}'s record.")
            else:
                print(f"Failure: Test result was not updated in patient #{self.__id}'s record.")
                return
        else:
            self.__test_results[(name, date)] = result
            print(f"Test result successfully added to patient #{self.__id}'s record.")

    def clear_test_results(self):
        self.__test_results.clear()


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
