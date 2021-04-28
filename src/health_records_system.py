class HealthRecordsSystem:

    def __init__(self):
        self.__patients = {}
        
    def add_patient(self, patient):
        if patient.ID in self.__patients:
            overwrite = input(f"Patient #{patient.ID} already exists. Overwrite? Y/N")
            if overwrite == "Y":
                self.__patients[patient.ID] = patient
                print(f"Patient #{patient.ID} successfully added to the system.")
            else:
                print(f"Failure: Patient #{patient.ID} was not added to the system.")
        else:
            self.__patients[patient.ID] = patient
            print(f"Patient #{patient.ID} successfully added to the system.")           
        
    def remove_patient(self, ID):
        try:
            del self.__patients[ID]
        except KeyError:
            print(f"Patient #{patient.ID} could not be removed because it does not exist in the system.")

    def print_patients(self):
        for (name, info) in self.__patients.items():
            print(f"Patient: {name}, Information: {info}")

class Patient:
    def __init__(self, ID, name, age):
        self.__ID = ID
        self.__name = name
        self.__age = age

    @property
    def ID(self):
        return self.__ID

        
