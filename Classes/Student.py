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
       self.schedule=[]

    def searchCourse(self, courseInfo ):
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ? OR TITLE= ?  """, (courseInfo, courseInfo))

        query_result = cursor.fetchone()
        return query_result 

    def addCourse(self, courseName):
       self.schedule.append(courseName)
       #cursor.execute("""SELECT *  FROM COURSE WHERE CRN = ?""", (CRN))
       #print(f"{self.firstName} added the course: {CRN} to his/her schedule.")
       #query_result = cursor.fetchone()
       #self.schedule.append(query_result[1])#add course title to the schedule list
       # I, Abdullahi I. added these to the code. Yet to be finalized

    def dropCourse(self, courseName):
       # cursor.execute("""SELECT *  FROM COURSE WHERE CRN = ?;""", (CRN))
       # print(f"{self.firstName} dropped the course: {CRN} from his/her schedule.")
       # query_result = cursor.fetchone()
       # self.schedule.remove(query_result[1])#remove course title to the schedule list
        # I, Abdullahi I. added these to the code. Yet to be finalized 

        self.schedule.remove(courseName)


    def printSchedule(self):
        pass
