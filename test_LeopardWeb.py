from main import *
import unittest
from unittest.mock import patch 
from Classes.Student import Student
from Classes.Instructor import Instructor
from dbConnection import *

#Creating a test class for main (Log in/log out)


#Creating a Test Class for the Instructor Class Functions
class Test_Instructor(unittest.TestCase):
    def setUp(self):
        self.instructor1 = Instructor("Marisha", "Rawlins", 10011)
   
    def tearDown(self):
        pass
    
    #def test_printSchedule(self):
    #    pass

    #def test_printClassList(self):
    #    pass
    
    def test_searchCourse(self):
        query_result = self.instructor1.searchCourse(3150)
        self.assertTrue(len(query_result)>0)
        self.assertEqual(query_result[0], 3150) 
        self.assertEqual(query_result[1], "OBJECT ORIENTED PROGRAMMING")

#Create a test class for admin
class Test_Admin(unittest.TestCase):
    def setUp(self):
        self.admin1= Admin("Vera", "Rubin", 30002)
    
    def tearDown(self):
        pass
    
    
    def test_addCourseToSystem(self):
        pass
        
  
   
    def test_removeCourseFromSystem(self):
        pass

    def test_searchCourse(self):
        query_result = self.admin1.searchCourse(3150)
        self.assertTrue(len(query_result)>0)
        self.assertEqual(query_result[0], 3150) 
        self.assertEqual(query_result[1], "OBJECT ORIENTED PROGRAMMING")

# Create a test class for student
class Test_Student(unittest.TestCase):
    
    def setUp(self):
        self.student1 = Student("Abdul", "Ibrahim", 10011)


    def tearDown(self):
        pass
    
    def test_searchCourse(self):
        query_result = self.student1.searchCourse(3150)
        self.assertTrue(len(query_result)>0)
        self.assertEqual(query_result[0], 3150) 
        self.assertEqual(query_result[1], "OBJECT ORIENTED PROGRAMMING")

    def test_addCourse(self):
        self.student1.addCourse("Signal and Systems")
        self.assertTrue(len(self.student1.schedule)>0) 
        self.assertEqual(self.student1.schedule[0], "Signal and Systems")

    def test_dropCourse(self):
        self.student1.addCourse("Engineering Senior Design")
        self.assertTrue(len(self.student1.schedule)>0) 
        self.student1.dropCourse("Engineering Senior Design")
        self.assertTrue(len(self.student1.schedule)==0)
        

if __name__ == '__main__':
    unittest.main()