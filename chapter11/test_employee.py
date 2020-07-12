from employee import Employee
import unittest

class test_Employee(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee('Steven','Jobs',5000000)
    
    def test_give_default_raise(self):
        self.employee1.give_raise(100)
        self.assertEqual(self.employee1.salary,5000100)
    
    def test_give_custom_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.salary,5005000)

unittest.main()