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

    def addCourseToSystem(self, courseName):
        print(f"You have added the course {courseName} to the system.\n")

    def removeCourseToSystem(self, courseName):
        print(f"You have removed the course {courseName} from the system.\n")

    def addUser(self, firstName, lastName, ID, userType):
        print(f"You have add a new {userType} to the system\n")

    def removeUser(self, userID):
        print(
            f"You have removed the user with UserID: {userID} from the system\n")

    def addStudentToCourse(self, studentID, courseName):
        print(f"You have added a new student to the course: {courseName}.\n")

    def removeStudentFromCourse(self, studentID, courseName):
        print(f"You have removed a student from the course: {courseName}\n")

    def searchCourseAndPrintRoster(self, courseInfo):
        print(f"The roster for the course {courseInfo} is:\n")
        print(f"Student 1 - Student 2 - ...........")

        #search
        cursor.execute("""SELECT * FROM COURSE WHERE CRN OR TITLE = ? """, (courseInfo))

        query_result = cursor.fetchone()
        return query_result 