from tkinter import messagebox
from tkinter import font
from tkinter import OptionMenu
from tkcalendar import Calendar
from datetime import date
import tkinter as tk
import functions

UserErrMsg = "User not found!"
InputErrMsg = "Check your data!"

class mainGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.titlefont = font.Font(family = "Arial", size = 16, weight = "bold")
        self.title("Weight Tracker")
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        self.global_name = tk.StringVar()
        self.global_gender = tk.StringVar()
        self.global_DOB = tk.StringVar()
        self.global_age = tk.StringVar()
        self.global_weight = tk.StringVar()
        self.global_height = tk.StringVar()
        self.global_BMI = tk.StringVar()
        self.global_status = tk.StringVar()
        self.frames = {}
        for i in (WelcomePage, ExistingUserPage, NewUserPage, ViewPage, DeletePage, AppendPage):
            frame = i(parent = container, controller = self)
            self.frames[i] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(WelcomePage)
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class WelcomePage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Weight Tracker", font = controller.titlefont)
        label.pack()
        
        self.NameLabel = tk.Label(self,text = "First and Last Name", font = ('calibre',10,'bold'))
        self.NameEntry = tk.Entry(self, textvariable = controller.global_name, font = ('calibre',10,'normal'))
        self.NameLabel.pack()
        self.NameEntry.pack()

        self.submitButton = tk.Button(self, text = "Login", command = lambda:[userCheck(controller.global_name.get())])
        self.newUserButton = tk.Button(self, text = "New User", command = lambda:controller.show_frame(NewUserPage))
        self.submitButton.pack()
        self.newUserButton.pack()
        
        def userCheck(temp_name):
            if functions.validateUser(temp_name) != True:
                messagebox.showinfo(title = "Error!", message = UserErrMsg)
            else:
                temp_name = controller.global_name.get()
                functions.setName(temp_name)
                functions.defineData(temp_name)
                controller.show_frame(ExistingUserPage)
                
class NewUserPage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        
        def dataCheck():
            temp_name = controller.global_name.get()
            temp_gender = controller.global_gender.get()
            temp_DOB = self.DOBCalendar.get_date()
            temp_weight = controller.global_weight.get()
            temp_height = controller.global_height.get()

            if len(temp_name) == 0 or temp_weight.isnumeric() == False or temp_height.isnumeric() == False:
                messagebox.showinfo(title = "Error!", message = InputErrMsg)
            else:
                functions.setData(temp_name, temp_gender, temp_DOB, temp_weight, temp_height)
                controller.show_frame(ExistingUserPage)
                
        options = [
            "Male",
            "Female"
        ]
        controller.global_gender.set(options[0])
        
        today = date.today()
        
        self.label = tk.Label(self, text = "New User", font = controller.titlefont)
        self.label.pack()
        
        self.NameLabel = tk.Label(self,text = "First and Last Name", font = ('calibre',10,'bold'))
        self.NameEntry = tk.Entry(self, textvariable = controller.global_name, font = ('calibre',10,'normal'))
        self.NameLabel.pack()
        self.NameEntry.pack()
        
        self.genderMenuLabel = tk.Label(self, text = "Gender:")
        self.genderMenu = OptionMenu(self, controller.global_gender, *options)
        self.genderMenuLabel.pack()
        self.genderMenu.pack()

        self.DOBLabel = tk.Label(self, text = "Date of Birth:")
        self.DOBCalendar = Calendar(self, selectmode = 'day', year = today.year, month = today.month, day = today.day)
        self.DOBLabel.pack()
        self.DOBCalendar.pack()
        
        self.weightLabel = tk.Label(self, text = "Weight:")
        self.weightEntry = tk.Entry(self, textvariable = controller.global_weight)
        self.weightLabel.pack()
        self.weightEntry.pack()
        
        self.heightLabel = tk.Label(self, text = "Height:")
        self.heightEntry = tk.Entry(self, textvariable = controller.global_height)
        self.heightLabel.pack()
        self.heightEntry.pack()
        
        self.submitButton = tk.Button(self, text = "Submit", command = dataCheck)
        self.submitButton.pack()
        
class ExistingUserPage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def defineVariable():
            controller.global_name.set(functions.getName()),
            controller.global_gender.set(functions.getGender()),
            controller.global_DOB.set(functions.getDOB()),
            controller.global_age.set(functions.getAge()),
            controller.global_weight.set(functions.getWeight()),
            controller.global_height.set(functions.getHeight()),
            controller.global_BMI.set(functions.getBMI()),
            controller.global_status.set(functions.getStatus())
        
        self.label = tk.Label(self, text = "Existing Users", font = controller.titlefont)
        self.label.pack()
        self.appendButton = tk.Button(self, 
                                      text = "Edit Data", 
                                      command = lambda:[
                                        controller.show_frame(AppendPage), 
                                        defineVariable()
                                        ])
        self.appendButton.pack()
        self.deleteButton = tk.Button(self, text = "Delete Data", command = lambda:controller.show_frame(DeletePage))
        self.deleteButton.pack()
        self.viewButton = tk.Button(self, 
                                    text = "View Data", 
                                    command = lambda:[
                                        controller.show_frame(ViewPage), 
                                        defineVariable()
                                        ])
        self.viewButton.pack()
        
        self.logoutButton = tk.Button(self, text = "Log out", command = lambda:controller.show_frame(WelcomePage))
        self.logoutButton.pack()

class ViewPage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        self.label = tk.Label(self, text = "View Data", font = controller.titlefont)
        self.label.pack()
        
        self.nameLabel = tk.Label(self, text = "NAME:")
        self.nameEntry = tk.Entry(self, textvariable = controller.global_name, state = "disabled")
        self.nameLabel.pack()
        self.nameEntry.pack()
        
        self.genderLabel = tk.Label(self, text = "GENDER:")
        self.genderEntry = tk.Entry(self, textvariable = controller.global_gender, state = "disabled")
        self.genderLabel.pack()
        self.genderEntry.pack()
        
        self.DOBLabel = tk.Label(self, text = "DATE OF BIRTH:")
        self.DOBEntry = tk.Entry(self, textvariable = controller.global_DOB, state = "disabled")
        self.DOBLabel.pack()
        self.DOBEntry.pack()
        
        self.ageLabel = tk.Label(self, text = "AGE:")
        self.ageEntry = tk.Entry(self, textvariable = controller.global_age, state = "disabled")
        self.ageLabel.pack()
        self.ageEntry.pack()
        
        self.weightLabel = tk.Label(self, text = "WEIGHT:")
        self.weightEntry = tk.Entry(self, textvariable = controller.global_weight, state = "disabled")
        self.weightLabel.pack()
        self.weightEntry.pack()
        
        self.heightLabel = tk.Label(self, text = "HEIGHT:")
        self.heightEntry = tk.Entry(self, textvariable = controller.global_height, state = "disabled")
        self.heightLabel.pack()
        self.heightEntry.pack()
        
        self.BMILabel = tk.Label(self, text = "BMI:")
        self.BMIEntry = tk.Entry(self, textvariable = controller.global_BMI, state = "disabled")
        self.BMILabel.pack()
        self.BMIEntry.pack()
        
        self.statusLabel = tk.Label(self, text = "STATUS:")
        self.statusEntry = tk.Entry(self, textvariable = controller.global_status, state = "disabled")
        self.statusLabel.pack()
        self.statusEntry.pack() 
        
        self.backButton = tk.Button(self, text = "Back to Menu", command = lambda:controller.show_frame(ExistingUserPage))
        self.backButton.pack()

class DeletePage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        
        self.label = tk.Label(self, text = "Delete Data", font = controller.titlefont)
        self.label.pack()   
        
        self.approveButton = tk.Button(self, text = "Confirm", command = lambda:functions.deleteData(controller.global_name.get()))
        self.approveButton.pack()
        self.backButton = tk.Button(self, text = "Back to Menu", command = lambda:controller.show_frame(ExistingUserPage))
        self.backButton.pack()

class AppendPage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 
        def dataCheck():
            temp_name = controller.global_name.get()
            temp_gender = controller.global_gender.get()
            temp_weight = controller.global_weight.get()
            temp_height = controller.global_height.get()

            if len(temp_name) == 0 or temp_weight.isnumeric() == False or temp_height.isnumeric() == False:
                messagebox.showinfo(title = "Error!", message = InputErrMsg)
            else:
                functions.computeBMI(temp_weight, temp_height)
                temp_BMI = functions.getBMI()
                functions.computeStatus(temp_BMI)
                temp_status = functions.getStatus()
                temp_DOB = functions.getDOB()
                controller.global_DOB.set(temp_DOB)
                controller.global_BMI.set(temp_BMI)
                controller.global_status.set(temp_status)
                functions.appendData(temp_name, temp_gender, temp_weight, temp_height)
                controller.show_frame(ExistingUserPage)
                
        self.label = tk.Label(self, text = "View Data", font = controller.titlefont)
        self.label.pack()
        
        self.nameLabel = tk.Label(self, text = "NAME:")
        self.nameEntry = tk.Entry(self, textvariable = controller.global_name, state = "disabled")
        self.nameLabel.pack()
        self.nameEntry.pack()
        
        self.genderLabel = tk.Label(self, text = "GENDER:")
        self.genderEntry = tk.Entry(self, textvariable = controller.global_gender)
        self.genderLabel.pack()
        self.genderEntry.pack()
        
        self.DOBLabel = tk.Label(self, text = "DATE OF BIRTH:")
        self.DOBEntry = tk.Entry(self, textvariable = controller.global_DOB, state = "disabled")
        self.DOBLabel.pack()
        self.DOBEntry.pack()
        
        self.ageLabel = tk.Label(self, text = "AGE:")
        self.ageEntry = tk.Entry(self, textvariable = controller.global_age, state = "disabled")
        self.ageLabel.pack()
        self.ageEntry.pack()
        
        self.weightLabel = tk.Label(self, text = "WEIGHT:")
        self.weightEntry = tk.Entry(self, textvariable = controller.global_weight)
        self.weightLabel.pack()
        self.weightEntry.pack()
        
        self.heightLabel = tk.Label(self, text = "HEIGHT:")
        self.heightEntry = tk.Entry(self, textvariable = controller.global_height)
        self.heightLabel.pack()
        self.heightEntry.pack()
        
        self.BMILabel = tk.Label(self, text = "BMI:")
        self.BMIEntry = tk.Entry(self, textvariable = controller.global_BMI, state = "disabled")
        self.BMILabel.pack()
        self.BMIEntry.pack()
        
        self.statusLabel = tk.Label(self, text = "STATUS:")
        self.statusEntry = tk.Entry(self, textvariable = controller.global_status, state = "disabled")
        self.statusLabel.pack()
        self.statusEntry.pack() 
        
        self.submitButton = tk.Button(self, text = "Submit", command = dataCheck)
        self.submitButton.pack()
        
        self.backButton = tk.Button(self, text = "Back to Menu", command = lambda:controller.show_frame(ExistingUserPage))
        self.backButton.pack()
        
app = mainGUI()
app.geometry("500x500")
app.mainloop() 
