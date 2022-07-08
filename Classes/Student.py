from Classes.User import User
import sqlite3
import sys
# setting path
sys.path.append('../LeopardWeb')
from dbConnection import *

class Student(User):
    # constructor
    def __init__(self, firstName, lastName, ID):
       super().__init__(firstName,lastName, ID)

    def searchCourse(self, courseInfo ):
        # print(f"{self.firstName} is looking for the course: {courseInfo} ....\n")
        # cursor.execute("""SELECT * FROM COURSE WHERE CRN, DAY, TIME = ? """, (courseInfo))
        # cursor.execute("""SELECT * FROM COURSE WHERE DAY = ? """, (courseInfo))
        # cursor.execute("""SELECT * FROM COURSE WHERE TIME = ? """, (courseInfo))
        # cursor.execute("""SELECT * FROM COURSE WHERE DEPARTMENT = ? """, (courseInfo))
        cursor.execute("""SELECT * FROM COURSE WHERE CRN OR TITLE = ? """, (courseInfo))

        query_result = cursor.fetchone()
        return query_result 

    def addCourse(self, courseName):
        print(f"{self.firstName} added the course: {courseName} to his/her schedule.")

    def dropCourse(self, courseName):
        print(f"{self.firstName} dropped the course: {courseName} from his/her schedule.")

    def printSchedule(self):
        print(f"{self.firstName} is printing his/her schedule....")
