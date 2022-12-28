from datetime import date 
import json
from tkinter import * 
"""
    This program will be used to track your:
        - Weight
        - Average Weight over all records -- Finished
        - Height
        - BMI -- Finished
        - Average BMI over all records -- Finished
        - If you are underweight, overweight, obese, etc according to the BMI scale -- WIP
        - It'll ask for your name and gender to ensure proper calculations, 
          this will be stored and not needed after the first program running
        - Age from date of birth -- Finished
        - New users will be able to be added, the program will ask you on start up which user, or new user
        - All of this information will be stored in a json file named Users.json
"""
def gui():
    window = Tk()
    window.geometry('400x300')
    greeting = Tk.title(text = "Welcome to the Weight Tracker App!")
    greeting.pack()
    window.mainloop()

def writeJson(data):
    with open ("Users.json", "w") as file:
      json.dump(data, file, indent = 4)

def getBMI(height, weight):
    tempHeight = 0
    tempHeight = (height * height)
    tempBMI = (weight / tempHeight) * 703
    BMI = round(tempBMI, 2)
    return BMI

def getAvgBMI(BMI):
    tempBMI = BMI
    avgBMI = sum(tempBMI) / len(tempBMI)
    print(avgBMI, round(avgBMI, 2))
    return avgBMI 

def getAvgWeight(weight):
    avgWeight = sum(weight) / len(weight)
    print(avgWeight, round(avgWeight, 2))
    return avgWeight

def getWeightStatus(BMI):
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

def getAge(DOB):
    today = date.today()
    age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))
    print(age)
    return age

if __name__ == "__main__":
  gui()
  firstName = input("What is your first name? ")
  lastName = input("What is your last name? ")
  gender = input("What is your gender? ")
  DOB = input("What is your date of birth? (yyyy-mm-dd) ")
  year, month, day = DOB.split("-")
  age = getAge(date(int(year), int(month), int(day)))
  weight = input("What is your weight? ")
  height = input("What is your height? ")
  BMI = getBMI(62, 140)
  status = getWeightStatus(BMI)
  
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
