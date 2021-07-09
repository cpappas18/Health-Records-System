# Electronic Health Records System

Note: this project is ongoing, in the testing phase

An Electronic Health Records system implemented in Python to demonstrate object-oriented programming and software design patterns. 

# Design Patterns
* Command design pattern: This pattern is used to achieve undo and redo functionality. The Invoker passes command requests to the Receiver (the HealthRecordsSystem class) and commands are defined by the ICommand interface. Concrete commands include AddPatient, RemovePatient, AddMedication, RemoveMedication, and AddTestResults. This pattern is advantageous because it allows for tracking operations history, it ensures the separation of concerns so that objects serve as manageable units of functionality, and it supports efficient scalability of the system because new commands can be added without changing existing code. 
* Singleton design pattern: This pattern is used to restrict the client to only one instantiation of the HealthRecordsSystem class and ensures global accessibility to this object. The pattern is appropriate for this application because only one system is needed to hold all patient information and access to this instance in different parts of the code is crucial.

# System Functionality
Users are able to...
* View patient records
* Add new patients
* Delete existing patients 
* Undo and redo previous actions
* Get patient contact information
* View patient medication, including dosage and frequency
* Add and remove patient medication
* View patient test results
* Add patient test results

# Using the System
To run the program, please use the command `python3 main.py`.

# Unit Testing
Test modules have been written to thoroughly test the program for errors. If any issues are found, please feel free to add your own tests and merge them with the main branch. 

To run the tests, please use the command `python3 -m unittest`.

# Public Disclosure
This project was created for practice and experimentation in software design and users must be aware that confidential patient information is not secure in this system. I do not take risk nor responsibility for any legal issues that arise from the usage of this software.

# References
https://medium.com/design-patterns-in-python/undo-redo-pattern-in-python-70ade29644b3
https://levelup.gitconnected.com/unit-testing-with-python-736112619620
