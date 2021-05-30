from health_records_system import *
from command import *


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
            med_name = input("Please input the name of the medication: ")
            dosage = input("Please input the dosage: ")
            frequency = input("Please input the frequency of this dosage: ")
            med = Medication(med_name, dosage, frequency)
            INVOKER.execute(ADD_MEDS, patient, med)

        elif option == 4:
            med_name = input("Please input the name of the medication: ")
            if med_name in patient.medication.keys():
                INVOKER.execute(REMOVE_MEDS, patient, patient.medication[med_name])
            else:
                print(f"Failure: Medication does not exist in patient #{patient.id}'s record.")
                return

        elif option == 5:
            for (name, date), result in patient.test_results.items():
                print(f"Test: {name}, Date: {date}, Result: {result}\n")

        elif option == 6:
            test_name = input("Please input the name of the test: ")
            date = input("Please input the date that the test was performed (DD/MM/YYYY): ")
            result = input("Please input the test result: ")
            INVOKER.execute(ADD_TEST_RESULTS, patient, test_name, date, result)

        elif option == 7:
            return

        else:
            print("Please enter a number between 1 and 7.")


if __name__ == "__main__":

    SYSTEM = HealthRecordsSystem()  # instantiate Receiver in Command design pattern

    # create commands
    ADD_PATIENT = AddPatientCommand(SYSTEM)
    REMOVE_PATIENT = RemovePatientCommand(SYSTEM)
    ADD_MEDS = AddMedicationCommand(SYSTEM)
    REMOVE_MEDS = RemoveMedicationCommand(SYSTEM)
    ADD_TEST_RESULTS = AddTestResultsCommand(SYSTEM)

    # register commands with Invoker
    INVOKER = Invoker()
    INVOKER.register(ADD_PATIENT)
    INVOKER.register(REMOVE_PATIENT)
    INVOKER.register(ADD_MEDS)
    INVOKER.register(REMOVE_MEDS)
    INVOKER.register(ADD_TEST_RESULTS)

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
            try:
                patient = SYSTEM.get_patient(id)
            except KeyError:
                print(f"Patient #{id} does not exist in the System.")
                continue

        if option == 1:
            view_edit_records(patient)

        elif option == 2:
            name = input("Please input the patient's name: ")
            age = input("Please input the patient's age: ")
            phone_number = input("Please input the patient's telephone number: ")
            patient = Patient(id, name, age, phone_number)
            INVOKER.execute(ADD_PATIENT, patient)

        elif option == 3:
            INVOKER.execute(REMOVE_PATIENT, patient)

        elif option == 4:
            print("Thank you for using the Electronic Health Records System!")
            break

        else:
            print("Please enter a number between 1 and 4.")
