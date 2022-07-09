from Classes.User import User
import sqlite3
import sys
# setting path
sys.path.append('../LeopardWeb')
from dbConnection import *

class Admin(User):
    # constructor
    def __init__(self, firstName, lastName, ID):
        super().__init__(firstName,lastName, ID)

    def addCourseToSystem(self, CRN, title, department, time, day, semester, year, credits):
        cursor.execute("""INSERT OR IGNORE INTO COURSE (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDITS ) VALUES (?,?,?,?,?,?,?,?) """, (CRN, title, department, time, day, semester, year, credits))
       # print(f"You have added the course {TITLE} to the system.\n")
       # cursor.execute("""INSERT INTO COURSE VALUES ?, ?, ?, ?, ?, ?, ?, ? """, (CRN, TITLE, DEPARTMENT, TIME, DAY, SEMESTER, YEAR, CREDITS))
        #Abdul made edits here, stil in progress
        
    def removeCourseFromSystem(self, CRNin):
        cursor.execute("""DELETE FROM COURSE WHERE CRN = ? """, (CRNin,))
        #print(f"You have removed the course {TITLE} from the system.\n")
        #cursor.execute("""DELETE FROM COURSE WHERE CRN or TITLE = ?, ? """, (CRN, TITLE))
        #Abdul made edits here 
        
    def addUser(self, firstName, lastName, ID, userType):
        print(f"You have add a new {userType} to the system\n")

  #  def addStudentUser(self, ID, NAME, SURNAME, GRADYEAR, MAJOR, EMAIL):
  #      print(f"You have add a new Student to the system\n")
  #      cursor.execute("""INSERT INTO COURSE VALUES ?, ?, ?, ?, ?, ? """, (ID, NAME, SURNAME, GRADYEAR, MAJOR, EMAIL))

  #  def addInstructorUser(self, ID, NAME, SURNAME, TITLE, HIREYEAR, DEPT, EMAIL):
  #      print(f"You have add a new Instructor to the system\n")
   #     cursor.execute("""INSERT INTO COURSE VALUES ?, ?, ?, ?, ?, ?, ? """, (ID, NAME, SURNAME, TITLE, HIREYEAR, DEPT, EMAIL))

  #  def addAdminUser(self, ID, NAME, SURNAME, TITLE, OFFICE, EMAIL):
  #      print(f"You have added a new admin to the system\n")
   #     cursor.execute("""INSERT INTO COURSE VALUES ?, ?, ?, ?, ?, ? """, (ID, NAME, SURNAME, TITLE, OFFICE, EMAIL))
   #Abdul made edits above with the comments
        
        
        
    def removeUser(self, userID):
        print(
            f"You have removed the user with UserID: {userID} from the system\n")

    #def removeStudentUser(self, ID):
     #   print(f"You have deleted a Student from the system\n")
      #  cursor.execute("""DELETE FROM STUDENT WHERE ID = ? """, (ID))

   # def removeInstructorUser(self, ID):
    #    print(f"You have deleted an instructor from the system\n")
     #   cursor.execute("""DELETE FROM INSTRUCTOR WHERE ID = ? """, (ID))

   # def removeAdminUser(self, ID):
    #    print(f"You have deleted an admin from the system\n")
     #   cursor.execute("""DELETE FROM ADMIN WHERE ID = ? """, (ID))
   #Abdul made edits above here as well
        
        
        
        
        
    def addStudentToCourse(self, studentID, courseName):
        print(f"You have added a new student to the course: {courseName}.\n")

    def removeStudentFromCourse(self, studentID, courseName):
        print(f"You have removed a student from the course: {courseName}\n")

    def searchCourse(self, courseInfo):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ? OR TITLE= ?  """, (courseInfo, courseInfo))

        query_result = cursor.fetchone()
        return query_result 

