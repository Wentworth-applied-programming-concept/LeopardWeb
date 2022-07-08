from Classes.User import User

class Instructor(User):
    # constructor
    def __init__(self, firstName, lastName, ID):
       super().__init__(firstName,lastName, ID)

    def printSchedule(self):
        print(f"Prof. {self.lastName} is printing his/her schedule....")

    def printClassList(self):
        print(
            f"Prof. {self.lastName} has the following class to teach this semester ....")

    def searchCourse(self, courseName):
        print(
            f"Prof. {self.lastName} is looking for the course: {courseName} ....\n")
