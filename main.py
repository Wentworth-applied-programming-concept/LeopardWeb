from unittest import result
from dbConnection import *
from Classes.User import User
from Classes.Admin import Admin
from Classes.Instructor import Instructor
from Classes.Student import Student

from tkinter import *
from tkinter import messagebox
from tkinter import ttk



def Dummy():
    pass



def logInAsAdmin():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM ADMIN WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    adminUser = Admin(dbRow[1],dbRow[2],dbRow[0])
    
    def goSearch():
        resultTable = ttk.Treeview(root)
        resultTable['columns']=("CRN", "Title", "Day", "Credits", "Semester")
        resultTable.column("#0", width=30)
        resultTable.column("CRN", width=50)
        resultTable.column("Title", width=200)
        resultTable.column("Day", width=30)
        resultTable.column("Credits", width=30)
        resultTable.column("Semester", width=50)
        
        resultTable.heading("#0", text="Check")
        resultTable.heading("CRN", text="CRN")
        resultTable.heading("Title", text="Title")
        resultTable.heading("Day", text="Day")
        resultTable.heading("Credits", text="Credits")
        resultTable.heading("Semester", text="Semester")
        
        
        mainCanvas.create_window(50,300, window=resultTable)
        
        
        
        
        
        
    
    def search():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Search Course by entering one of those param (any):",font=('Helvetica','14','bold'))
        mainCanvas.create_text(300, 100, text="CRN, Time, Day, Title ",font=('Helvetica','11'))
        mainCanvas.create_text(200, 140, text="Param: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 140, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=10 )
        mainCanvas.create_window(400, 140, window= goBttn)
        
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Admin "+ adminUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchAllBttn = Button(root, text="Search all Courses", font=('Helvetica','11'), command=search, width=30 )
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
    
    def goSearch():
        resultTable = ttk.Treeview(root, columns=(0,1,2,3,4,5), show='headings', height=5)
        resultTable.column(0, width=20)
        resultTable.column(1, width=60)
        resultTable.column(2, width=250)
        resultTable.column(3, width=50)
        resultTable.column(4, width=50)
        resultTable.column(5, width=70)
        
        resultTable.heading(0, text=" ")
        resultTable.heading(1, text="CRN")
        resultTable.heading(2, text="Title")
        resultTable.heading(3, text="Day")
        resultTable.heading(4, text="Credits")
        resultTable.heading(5, text="Semester")
        
        
        mainCanvas.create_window(270,300, window=resultTable)
        
    
    def search():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Search Course by entering one of those param (any):",font=('Helvetica','14','bold'))
        mainCanvas.create_text(300, 100, text="CRN, Time, Day, Title ",font=('Helvetica','11'))
        mainCanvas.create_text(200, 140, text="Param: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 140, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=20 )
        mainCanvas.create_window(300, 200, window= goBttn)
    
    def addCourse():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Add Course by entering CRN",font=('Helvetica','14','bold'))
        mainCanvas.create_text(200, 100, text="CRN: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 100, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=20 )
        mainCanvas.create_window(300, 200, window= goBttn)
        
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Admin "+ studentUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchBttn = Button(root, text="Search Courses", font=('Helvetica','11'), command=search, width=30 )
    mainCanvas.create_window(300, 200, window= searchBttn)
    addCourseBttn = Button(root, text="Add Course to schedule", font=('Helvetica','11'), command=addCourse, width=30 )
    mainCanvas.create_window(300, 250, window= addCourseBttn)
    removeCourseBttn = Button(root, text="Remove Course from schedule", font=('Helvetica','11'), command=Dummy, width=30 )
    mainCanvas.create_window(300, 300, window= removeCourseBttn)

def logInAsInstructor():
    mainCanvas.delete("all")
    
    cursor.execute(""" SELECT * FROM INSTRUCTOR WHERE EMAIL=? """, (userIDEntry.get(),))
    dbRow = cursor.fetchone()
    instructorUser = Instructor(dbRow[1],dbRow[2],dbRow[0])
    
    def goSearch():
        pass
    
    def search():
        mainCanvas.delete("all")
        mainCanvas.create_text(300, 30, text="Search Course by entering one of those param (any):",font=('Helvetica','14','bold'))
        mainCanvas.create_text(300, 100, text="CRN, Time, Day, Title ",font=('Helvetica','11'))
        mainCanvas.create_text(200, 140, text="Param: ",font=('Helvetica','11'))
        mainCanvas.create_window(340, 140, window=searchEntry) 
        goBttn = Button(root, text="Go", font=('Helvetica','11'), command=goSearch, width=20 )
        mainCanvas.create_window(300, 260, window= goBttn)
        
    mainCanvas.create_text(300, 30, text="Leopard Web accesed by: Prof. "+ instructorUser.firstName ,font=('Helvetica','14','bold'))
    mainCanvas.create_text(300, 100, text="Please select an item to continue: ",font=('Helvetica','11'))
    
    searchBttn = Button(root, text="Search Courses", font=('Helvetica','11'), command=search, width=30 )
    mainCanvas.create_window(300, 200, window= searchBttn)
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
    
    global userIDEntry, passwordEntry, searchEntry
    userIDEntry= Entry(root,font=('Helvetica','11'), width=20 ) 
    passwordEntry= Entry(root,show="*",font=('Helvetica','11'), width=20 ) 
    searchEntry= Entry(root,font=('Helvetica','11'), width=20 ) 
    
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