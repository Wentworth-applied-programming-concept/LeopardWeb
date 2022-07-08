from dbConnection import *
from Classes.User import User
from Classes.Admin import Admin
from Classes.Instructor import Instructor
from Classes.Student import Student

from tkinter import *
from tkinter import messagebox

#---Password----
# student = pass1235
# instr = pass1234
# admin = pass123


def Dummy():
    pass

def logInAsAdmin():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM ADMIN WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    adminUser = Admin(dbRow[1],dbRow[2],dbRow[0])
    
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Admin "+ adminUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchAllBttn = Button(root, text="Search all Courses", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 150, window= searchAllBttn)
    searchParamBttn = Button(root, text="Search Courses by parameters", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 200, window= searchParamBttn)
    addCourseBttn = Button(root, text="Add Course to system", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 250, window= addCourseBttn)
    removeCourseBttn = Button(root, text="Remove Course from system", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 300, window= removeCourseBttn)

def logInAsStudent():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM STUDENT WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    studentUser = Student(dbRow[1],dbRow[2],dbRow[0])
    
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: "+ studentUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchAllBttn = Button(root, text="Search all Courses", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 150, window= searchAllBttn)
    searchParamBttn = Button(root, text="Search Courses by parameters", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 200, window= searchParamBttn)
    addCourseBttn = Button(root, text="Add Course to schedule", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 250, window= addCourseBttn)
    removeCourseBttn = Button(root, text="Remove Course from schedule", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 300, window= removeCourseBttn)

def logInAsInstructor():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM INSTRUCTOR WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    instructorUser = Instructor(dbRow[1],dbRow[2],dbRow[0])
    
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Prof. "+ instructorUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchAllBttn = Button(root, text="Search all Courses", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 150, window= searchAllBttn)
    searchParamBttn = Button(root, text="Search Courses by parameters", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 200, window= searchParamBttn)
    addRemoveBttn = Button(root, text="Print Course Roster", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 200, window= addRemoveBttn)
    
    
def signIn():
    cursor.execute("SELECT * FROM ADMIN_LOGINS where username=? AND password=?",(userIDEntry.get(), passwordEntry.get()))
    logAdmin=cursor.fetchone()
    cursor.execute("SELECT * FROM INSTRUCTOR_LOGINS where username=? AND password=?",(userIDEntry.get(), passwordEntry.get()))
    logInstructor=cursor.fetchone()
    cursor.execute("SELECT * FROM STUDENT_LOGINS where username=? AND password=?",(userIDEntry.get(), passwordEntry.get()))
    logStudent=cursor.fetchone()
    
    if logAdmin:
        logInAsAdmin()
    elif logStudent:
        logInAsStudent()
    elif logInstructor:
        logInAsInstructor()
    else:
        messagebox.showinfo("info", "Login Failed.")
        



def main():
    createLogins()
    global root
    root=Tk()
    root.title('Leopard Web')
    root.geometry('600x500')
    root['padx']=20
    
    global mainCanvas
    mainCanvas = Canvas(root, width=400, height=400) #create canvas
    mainCanvas.pack(fill="both", expand=True)

    mainCanvas.create_text(300, 30, text="Welcome to Leopard Web",font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please enter your Username and password. ",font=('Helvetica','11'))
    
    global userIDEntry, passwordEntry
    userIDEntry= Entry(root,font=('Helvetica','11'), width=20 ) 
    passwordEntry= Entry(root,show="*",font=('Helvetica','11'), width=20 ) 

    mainCanvas.create_text(200, 140, text="Username: ",font=('Helvetica','11'))
    mainCanvas.create_window(340, 140, window=userIDEntry) 
    mainCanvas.create_text(200, 170, text="Password: ",font=('Helvetica','11'))
    mainCanvas.create_window(340, 170, window=passwordEntry) 

    global signInBttn
    signInBttn = Button(root, text="Sign In", font=('Helvetica','11'), command=signIn, width=20 )
    mainCanvas.create_window(300, 260, window= signInBttn)
    
    root.mainloop()

    #close the connection 
    database.commit() 
    database.close()


if __name__ == '__main__':
    main()