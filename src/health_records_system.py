class HealthRecordsSystem:

    def __init__(self):
        self.__patients = {}

    def get_patient(self, ID):
        return self.__patients[ID]

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
            print(f"Patient #{ID} successfully removed from the system.")
        except KeyError:
            print(f"Patient #{ID} does not exist in the system.")
            return
        
    def print_patients(self):
        for (name, info) in self.__patients.items():
            print(f"Patient: {name}, Information: {info}")

class Patient:
    def __init__(self, ID, name, age):
        self.__ID = ID
        self.__name = name
        self.__age = age
        self.__medication = {}        

    @property
    def ID(self):
        return self.__ID
    
    @property
    def medication(self):
        return self.__medication
    
    def add_medication(self, medication, dosage, frequency):
        if medication in self.__medication:
            overwrite = input(f"Patient #{patient.ID} is already taking this medication. Overwrite dosage and frequency? Y/N")
            if overwrite == "Y":
                self.__medication[medication] = (dosage, frequency)
                print(f"Medication successfully updated in patient #{ID}'s record.")
            else:
                print(f"Failure: Medication was not updated in patient #{ID}'s record.")
        else:
                self.__medication[medication] = (dosage, frequency)
                print(f"Medication successfully added to patient #{ID}'s record.")   
     

        
