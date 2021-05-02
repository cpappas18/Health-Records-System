from health_records_system import HealthRecordsSystem, Patient

def main():
    system = HealthRecordsSystem()
    
    while True:
        option = input("""
        ----- Electronic Health Records System -----
        Enter a number to select an option:
        1. View and edit patient records
        2. Add a new patient
        3. Delete a patient's file
        4. Cancel
        """)
    
        try:
            option = int(option)
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue
        
        if option != 4:
            ID = input("Please input the patient's ID number: ")

        if option == 1:
            try:
                patient = system.get_patient(ID)
                view_edit_records(patient)
            except KeyError:
                print(f"Patient #{ID} does not exist in the system.")
                continue

        elif option == 2:
            name = input("Please input the patient's name: ")
            age = input("Please input the patient's age: ")
            patient = Patient(ID, name, age)
            system.add_patient(patient)
        
        elif option == 3:
            system.remove_patient(ID)

        elif option == 4:
            print("Thank you for using the Electronic Health Records System!")
            return

        else:
            print("Please enter a number between 1 and 4.")

    
    
def view_edit_records(patient):
    while True:
        option = input("""
        ----- View and Edit Patient Records -----
            Enter a number to select an option:
            1. View medication
            2. Add medication
            3. Remove medication
            4. Cancel
            """)

        try:
            option = int(option)
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if option == 1:
            for medication, (dosage, frequency) in patient.medication.items():
                print(f"Medication: #{medication}, Dosage: #{dosage}, Frequency: #{frequency}\n")

        elif option == 2:
            medication = input("Please input the name of the medication: ")
            dosage = input("Please input the dosage: ")
            frequency = input("Please input the frequency of this dosage: ")
            patient.add_medication(medication, dosage, frequency)

if __name__ == "__main__":
    main()
