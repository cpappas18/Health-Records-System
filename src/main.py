from health_records_system import *
from command import *

# instantiate Receiver and Invoker for Command design pattern
SYSTEM = HealthRecordsSystem()
INVOKER = Invoker()

# create commands
ADD_PATIENT = AddPatientCommand(SYSTEM)
REMOVE_PATIENT = RemovePatientCommand(SYSTEM)
ADD_MEDS = AddMedicationCommand(SYSTEM)
REMOVE_MEDS = RemoveMedicationCommand(SYSTEM)
ADD_TEST_RESULTS = AddTestResultsCommand(SYSTEM)


def main():

    # register commands with Invoker
    INVOKER.register(ADD_PATIENT)
    INVOKER.register(REMOVE_PATIENT)
    INVOKER.register(ADD_MEDS)
    INVOKER.register(REMOVE_MEDS)
    INVOKER.register(ADD_TEST_RESULTS)

    while True:
        option = input("""
        ----- Electronic Health Records System -----
        1. View and edit patient records
        2. Add a new patient
        3. Delete a patient's file
        4. Undo last action
        5. Redo last action
        6. Cancel
        Enter a number to select an option:
        """)

        try:
            option = int(option)
        except ValueError:
            print("Please enter a number between 1 and 6.")
            continue

        if option == 1:
            id = input("Please input the patient's ID number: ")
            patient = SYSTEM.get_patient(id)

            if patient:
                view_edit_records(patient)

        elif option == 2:
            id = input("Please input the patient's ID number: ")
            name = input("Please input the patient's name: ")
            age = input("Please input the patient's age: ")
            phone_number = input("Please input the patient's telephone number: ")
            patient = Patient(id, name, age, phone_number)
            INVOKER.execute(ADD_PATIENT, patient)

        elif option == 3:
            id = input("Please input the patient's ID number: ")
            patient = SYSTEM.get_patient(id)

            if patient:
                INVOKER.execute(REMOVE_PATIENT, patient)

        elif option == 4:
            INVOKER.undo()

        elif option == 5:
            INVOKER.redo()

        elif option == 6:
            print("Thank you for using the Electronic Health Records System!")
            exit(0)

        else:
            print("Please enter a number between 1 and 6.")


def view_edit_records(patient):
    while True:
        option = input("""
        ----- View and Edit Patient Records -----
            1. View patient information
            2. View medication
            3. Add medication
            4. Remove medication
            5. View test results
            6. Add test results
            7. Undo last action
            8. Redo last action
            9. Cancel
            Enter a number to select an option:
            """)

        try:
            option = int(option)
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        if option == 1:
            print(f"Name: {patient.name}")
            print(f"Age: {patient.age}")
            print(f"Phone number: {patient.phone_number}")
            print(f"ID number: {patient.id}")

        elif option == 2:
            if len(patient.medication) > 0:
                for med_name, medication in patient.medication.items():
                    print(f"Medication: {med_name}, Dosage: {medication.dosage}, Frequency: {medication.frequency}")
            else:
                print("This patient is not taking any medication.")

        elif option == 3:
            med_name = input("Please input the name of the medication: ")
            dosage = input("Please input the dosage: ")
            frequency = input("Please input the frequency of this dosage: ")
            med = Medication(med_name, dosage, frequency)
            INVOKER.execute(ADD_MEDS, patient, med)

        elif option == 4:
            med_name = input("Please input the name of the medication: ")
            med = patient.get_medication(med_name)

            if med:
                INVOKER.execute(REMOVE_MEDS, patient, med_name)

        elif option == 5:
            view_option = input("To view all test results, type \"all\". "
                                "Otherwise, specify the test name and date that it was performed in the format \"name DD/MM/YYYY\". ")

            if view_option == "all":
                if len(patient.test_results) == 0:
                    print("This patient has no test results to display.")
                else:
                    for (test_name, date), result in patient.test_results.items():
                        print(f"Test: {test_name}, Date: {date}, Result: {result}\n")
            else:
                try:
                    test_name, date = view_option.split(" ")
                    result = patient.get_test_results(test_name, date)
                    if result:
                        print(f"Test: {test_name}, Date: {date}, Result: {result}\n")
                except ValueError:
                    print("The input is invalid. Please try again.")

        elif option == 6:
            test_name = input("Please input the name of the test: ")
            date = input("Please input the date that the test was performed (DD/MM/YYYY): ")
            result = input("Please input the test result: ")
            INVOKER.execute(ADD_TEST_RESULTS, patient, test_name, date, result)

        elif option == 7:
            INVOKER.undo()

        elif option == 8:
            INVOKER.redo()

        elif option == 9:
            return

        else:
            print("Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()

