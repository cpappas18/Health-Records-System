from health_records_system import HealthRecordsSystem, Patient

def main():
    system = HealthRecordsSystem()
    
    while True:
        option = input("""
        ----- Electronic Health Records System -----
        Enter a number to select an option:
        1. View patient records
        2. Add a new patient
        3. Delete a patient's file
        4. Cancel
        """)
    
        try:
            option = int(option)
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if option == 1:
            system.print_patients()
            
        elif option == 2:
            ID = input("Please input the patient's ID number: ")
            name = input("Please input the patient's name: ")
            age = input("Please input the patient's age: ")
            patient = Patient(ID, name, age)
            system.add_patient(patient)
        
        elif option == 3:
            remove_ID = input("Please input the ID number of the patient that you want to remove:")
            system.remove_patient(remove_ID)

        elif option == 4:
            break

        else:
            print("Please enter a number between 1 and 4.")

    
if __name__ == "__main__":
    main()
