from Classes.User import User

class Student(User):
    # constructor
    def __init__(self, firstName, lastName, ID):
       super().__init__(firstName,lastName, ID)

    def searchCourse(self, courseName):
        print(f"{self.firstName} is looking for the course: {courseName} ....\n")

    def addCourse(self, courseName):
        print(f"{self.firstName} added the course: {courseName} to his/her schedule.")

    def dropCourse(self, courseName):
        print(f"{self.firstName} dropped the course: {courseName} from his/her schedule.")

    def printSchedule(self):
        print(f"{self.firstName} is printing his/her schedule....")
