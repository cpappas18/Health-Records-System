import mock
import builtins
from unittest import TestCase
from src.health_records_system import *


class TestHealthRecordsSystem(TestCase):

    def setUp(self):
        self.system = HealthRecordsSystem()

    def tearDown(self):
        HealthRecordsSystem._reset()

    def test_get_instance(self):
        instance = HealthRecordsSystem.get_instance()
        self.assertEqual(instance, self.system)

    def test_get_patient_for_valid_id(self):
        patient = Patient(1, "Jane", 20, 123)
        self.system.add_patient(patient)
        self.assertEqual(self.system.get_patient(1), patient)

    def test_get_patient_for_invalid_id(self):
        self.assertEqual(self.system.get_patient(1), None)

    def test_add_patient_already_exists_overwrite(self):
        patient1 = Patient(1, "Jane", 20, 123)
        self.system.add_patient(patient1)
        patient2 = Patient(1, "John", 20, 123)

        with mock.patch.object(builtins, 'input', lambda _: 'Y'):
            self.system.add_patient(patient2)
            self.assertEqual(self.system._patients, {1: patient2})

    def test_add_patient_already_exists_no_overwrite(self):
        patient1 = Patient(1, "Jane", 20, 123)
        self.system.add_patient(patient1)
        patient2 = Patient(1, "John", 20, 123)

        with mock.patch.object(builtins, 'input', lambda _: 'N'):
            self.system.add_patient(patient2)
            self.assertEqual(self.system._patients, {1: patient1})

    def test_add_patient_new(self):
        patient = Patient(1, "Jane", 20, 123)
        self.system.add_patient(patient)
        self.assertEqual(self.system._patients, {1: patient})

    def test_remove_patient_for_valid_id(self):
        patient = Patient(1, "Jane", 20, 123)
        self.system.add_patient(patient)
        self.system.remove_patient(1)
        self.assertEqual(self.system._patients, {})

    def test_remove_patient_for_invalid_id(self):
        result = self.system.remove_patient(1)
        self.assertEqual(result, None)


class TestPatient(TestCase):

    def setUp(self):
        self.patient = Patient(1, "Jane", 20, 123)

    def test_get_medication_for_valid_name(self):
        med = Medication("Advil", "1 tablet", "once a day")
        self.patient.add_medication(med)
        self.assertEqual(self.patient.get_medication("Advil"), med)

    def test_get_medication_for_invalid_name(self):
        self.assertEqual(self.patient.get_medication("Advil"), None)

    def test_add_medication_already_exists_overwrite(self):
        med1 = Medication("Advil", "1 tablet", "once a day")
        self.patient.add_medication(med1)
        med2 = Medication("Advil", "1 tablet", "twice a day")

        with mock.patch.object(builtins, 'input', lambda _: 'Y'):
            self.patient.add_medication(med2)
            self.assertEqual(self.patient.medication, {"Advil": med2})

    def test_add_medication_already_exists_no_overwrite(self):
        med1 = Medication("Advil", "1 tablet", "once a day")
        self.patient.add_medication(med1)
        med2 = Medication("Advil", "1 tablet", "twice a day")

        with mock.patch.object(builtins, 'input', lambda _: 'N'):
            self.patient.add_medication(med2)
            self.assertEqual(self.patient.medication, {"Advil": med1})

    def test_add_medication_new(self):
        med = Medication("Advil", "1 tablet", "once a day")
        self.patient.add_medication(med)
        self.assertEqual(self.patient.medication, {"Advil": med})

    def test_remove_medication_for_valid_name(self):
        med = Medication("Advil", "1 tablet", "once a day")
        self.patient.add_medication(med)
        self.patient.remove_medication("Advil")
        self.assertEqual(self.patient.medication, {})

    def test_remove_medication_for_invalid_name(self):
        result = self.patient.remove_medication("Advil")
        self.assertEqual(result, None)

    def test_clear_medication(self):
        med = Medication("Advil", "1 tablet", "once a day")
        self.patient.add_medication(med)
        self.patient.clear_medication()
        self.assertEqual(self.patient.medication, {})

    def test_get_test_results_for_valid_name_date(self):
        self.patient.add_test_results("COVID", "June 26, 2021", "Negative")
        self.assertEqual(self.patient.get_test_results("COVID", "June 26, 2021"), "Negative")

    def test_get_test_results_for_invalid_name_date(self):
        self.assertEqual(self.patient.get_test_results("COVID", "June 26, 2021"), None)

    def test_add_test_results_already_exists_overwrite(self):
        self.patient.add_test_results("COVID", "June 26, 2021", "Negative")

        with mock.patch.object(builtins, 'input', lambda _: 'Y'):
            self.patient.add_test_results("COVID", "June 26, 2021", "Positive")
            self.assertEqual(self.patient.test_results, {("COVID", "June 26, 2021"): "Positive"})

    def test_add_test_results_already_exists_no_overwrite(self):
        self.patient.add_test_results("COVID", "June 26, 2021", "Negative")

        with mock.patch.object(builtins, 'input', lambda _: 'N'):
            self.patient.add_test_results("COVID", "June 26, 2021", "Positive")
            self.assertEqual(self.patient.test_results, {("COVID", "June 26, 2021"): "Negative"})

    def test_add_test_results_new(self):
        self.patient.add_test_results("COVID", "June 26, 2021", "Negative")
        self.assertEqual(self.patient.test_results, {("COVID", "June 26, 2021"): "Negative"})

    def test_clear_test_results(self):
        self.patient.add_test_results("COVID", "June 26, 2021", "Negative")
        self.patient.clear_test_results()
        self.assertEqual(self.patient.test_results, {})
