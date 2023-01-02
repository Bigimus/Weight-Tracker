from tkinter import messagebox
from tkinter import font
from tkinter import OptionMenu
from tkcalendar import Calendar
from datetime import date
import Weight_Tracker as WT
import tkinter as tk
import json

errMsg = "User not found!"

def writeJson (data):
    with open ("Users.json", "w") as file:
      json.dump(data, file, indent = 4)

def getAge(DOB):
    today = date.today()    
    age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))
    return age

def getBMI(height, weight):
    tempHeight = 0
    tempHeight = (int(height) * int(height))
    tempBMI = (int(weight) / tempHeight) * 703
    BMI = round(tempBMI, 2)
    return BMI

def getStatus(BMI):
  #Have to add gender and age specification
    tempBMI = BMI
    if tempBMI >= 0 and tempBMI <= 18.5:
      status = "Underweight"
    if tempBMI > 18.5 and tempBMI <= 25:
      status = "Healthy"
    if tempBMI > 25 and tempBMI <= 30:
      status = "Overweight"
    if tempBMI > 30:
      status = "Obese"
    return status

def getData(firstName, lastName):
    with open ("Users.json", "r") as file:
      tempData = json.load(file)
      #Have to check all first + last names.
      FN_List = []
      LN_List = []
      for users in tempData["Users"]:
        FN_List.append(users["First Name"])
        LN_List.append(users["Last Name"])
      #Verifies real users. 
      for i in FN_List:
        if firstName.lower() == i.lower():
            for j in LN_List:
                if lastName.lower() == j.lower(): return True  
                else: continue
        else: continue
        
def setData(firstName, lastName, gender, DOB, weight, height):
    month, day, year = DOB.split("/")
    year = int(year) + 2000
    age = getAge(date(int(year), int(month), int(day)))
    BMI = getBMI(height, weight)
    status = getStatus
    with open ("Users.json") as file:
        data = json.load(file)
        temp = data["Users"]
        newUser = {
            "First Name": firstName,
            "Last Name": lastName,
            "Gender": gender,
            "Date of Birth": DOB,
            "Age": age,
            "Weight": weight,
            "Height": height,
            "BMI": BMI,
            "Status": status
        }
        temp.append(newUser)
    writeJson(data)

class mainGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.titlefont = font.Font(family = "Arial", size = 16, weight = "bold")
        self.title("Weight Tracker")
        container = tk.Frame()
        container.grid(row = 0, column = 0, sticky = 'nesw')
        
        self.tempFirstName = tk.StringVar()
        self.tempLastName = tk.StringVar()
        
        self.frames = {}
        
        for i in (WelcomePage, ExistingUserPage, NewUserPage):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0,column=0, sticky = "nesw")

        self.show_frame(WelcomePage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class WelcomePage(tk.Frame):
    
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text = "Weight Tracker", font = controller.titlefont)
        label.pack()

        #Controls the first name label and entry box. 
        self.firstNameLabel = tk.Label(self, text = "First Name", font = ('calibre',10,'bold'))
        self.firstNameEntry = tk.Entry(self, font = ('calibre',10,'normal'))
        #Controls the last name label and entry box.
        self.lastNameLabel = tk.Label(self, text = "Last Name", font = ('calibre',10,'bold'))
        self.lastNameEntry = tk.Entry(self, font = ('calibre', 10, 'normal'))
        #Controls the subit button
        self.submitButton = tk.Button(self, text = "Login", command = self.userCheck)
        #Controls the new user button. 
        self.newUserButton = tk.Button(self, text = "New User", command = lambda:controller.show_frame(NewUserPage))


        #Places each item on the GUI.
        self.firstNameLabel.pack()
        self.firstNameEntry.pack()
        self.lastNameLabel.pack()
        self.lastNameEntry.pack()
        self.submitButton.pack()
        self.newUserButton.pack()

    def userCheck(self):
        FN = self.firstNameEntry.get()
        LN = self.lastNameEntry.get()
            
        try:
            results = getData(FN, LN)
            if results != True:
                print(errMsg)
                raise Exception
            else:
                app.show_frame(ExistingUserPage)
                            
        except Exception: 
            messagebox.showinfo(title = "Error!", message = errMsg)
        
class ExistingUserPage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Existing Users", font = controller.titlefont)
        label.pack()
        appendButton = tk.Button(self, text="Edit Data", command = WT.appendData)
        deleteButton = tk.Button(self, text="Delete Data", command = WT.deleteData)
        viewDataButton = tk.Button(self, text="View Data", command = WT.viewData)
        viewTrendsButton = tk.Button(self, text="View Trends", command = WT.viewTrends)
        appendButton.pack()
        deleteButton.pack()
        viewDataButton.pack()
        viewTrendsButton.pack()

class NewUserPage(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "New User", font = controller.titlefont)
        label.pack()
        
        self.firstNameLabel = tk.Label(self, text = "First Name:", font = ('calibre',10,'bold'))
        self.firstNameEntry = tk.Entry(self, font = ('calibre',10,'normal'))

        self.lastNameLabel = tk.Label(self, text = "Last Name:", font = ('calibre',10,'bold'))
        self.lastNameEntry = tk.Entry(self, font = ('calibre', 10, 'normal'))
        
        options = [
            "Male",
            "Female"
        ]
        variable = tk.StringVar(self)
        variable.set(options[0])
        self.genderMenuLabel = tk.Label(self, text = "Gender:")
        self.genderMenu = OptionMenu(self, variable, *options)
        
        today = date.today()
        self.DOBLabel = tk.Label(self, text = "Date of Birth:")
        self.DOBCalendar = Calendar(self, selectmode = 'day', year = today.year, month = today.month, day = today.day)

        self.weightLabel = tk.Label(self, text = "Weight:")
        self.weightEntry = tk.Entry(self)
        
        self.heightLabel = tk.Label(self, text = "Height:")
        self.heightEntry = tk.Entry(self)
        
        self.submitButton = tk.Button(self, text = "Submit", command = lambda:setData(self.firstNameEntry.get(), self.lastNameEntry.get(), variable.get(), self.DOBCalendar.get_date(), self.weightEntry.get(), self.heightEntry.get()))
        
        self.firstNameLabel.pack()
        self.firstNameEntry.pack()       
        self.lastNameLabel.pack()
        self.lastNameEntry.pack()
        self.genderMenuLabel.pack()
        self.genderMenu.pack()
        self.DOBLabel.pack()
        self.DOBCalendar.pack()
        self.weightLabel.pack()
        self.weightEntry.pack()
        self.heightLabel.pack()
        self.heightEntry.pack()
        self.submitButton.pack()

app = mainGUI()
app.geometry("500x500")
app.mainloop()
