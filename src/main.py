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
            id = input("Please input the patient's ID number: ")

        if option == 1:
            try:
                patient = system.get_patient(id)
                view_edit_records(patient)
            except KeyError:
                print(f"Patient #{id} does not exist in the system.")
                continue

        elif option == 2:
            name = input("Please input the patient's name: ")
            age = input("Please input the patient's age: ")
            phone_number = input("Please input the patient's telephone number: ")
            patient = Patient(id, name, age, phone_number)
            system.add_patient(patient)
        
        elif option == 3:
            system.remove_patient(id)

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
            1. Get patient contact information
            2. View medication
            3. Add medication
            4. Remove medication
            5. View test results
            6. Add test results
            7. Cancel
            """)

        try:
            option = int(option)
        except ValueError:
            print("Please enter a number between 1 and 7.\n")
            continue

        if option == 1:
            print(f"Phone number: {patient.phone_number}")

        elif option == 2:
            for medication, (dosage, frequency) in patient.medication.items():
                print(f"Medication: {medication}, Dosage: {dosage}, Frequency: {frequency}\n")

        elif option == 3:
            medication_name = input("Please input the name of the medication: ")
            dosage = input("Please input the dosage: ")
            frequency = input("Please input the frequency of this dosage: ")
            patient.add_medication(medication_name, dosage, frequency)

        elif option == 4:
            medication_name = input("Please input the name of the medication: ")
            patient.remove_medication(medication_name)

        elif option == 5:
            for (name, date), result in patient.test_results.items():
                print(f"Test: {name}, Date: {date}, Result: {result}\n")

        elif option == 6:
            test_name = input("Please input the name of the test: ")
            date = input("Please input the date that the test was performed (DD/MM/YYYY): ")
            result = input("Please input the test result: ")
            patient.add_test_results(test_name, date, result)

        elif option == 7:
            return

        else:
            print("Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
