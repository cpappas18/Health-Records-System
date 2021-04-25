class HealthRecordsSystem:
    patients = []
    
    #def __init__(self):
        
    def add_patient(self, patient):
        self.patients[patient] = None


class Patient:
    def __init__(self, name):
        self.name = name
