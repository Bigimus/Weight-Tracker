from datetime import date
import tkinter as tk
import json

name = ""
gender = ""
DOB = ""
age = ""
weight = ""
height = ""
BMI = ""
status = ""

def writeUsers (data):
    with open ("Users.json", "w") as file:
      json.dump(data, file, indent = 4)
        
def setName(temp_name):
    global name
    name = temp_name

def setGender(temp_gender):
    global gender
    gender = temp_gender

def setDOB(temp_DOB):
    global DOB
    DOB = temp_DOB

def setAge(temp_age):
    global age
    age = temp_age

def setWeight(temp_weight):
    global weight
    weight = temp_weight

def setHeight(temp_height):
    global height
    height = temp_height

def setBMI(temp_BMI):
    global BMI
    BMI = temp_BMI

def setStatus(temp_status):
    global status
    status = temp_status
    
def getName():
    global name
    return name

def getGender():
    global gender
    return gender

def getDOB():
    global DOB
    return DOB

def getAge():
    global age
    return age

def getWeight():
    global weight
    return weight

def getHeight():
    global height
    return height

def getBMI():
    global BMI
    return BMI

def getStatus():
    global status
    return status

def getData():
    with open ("Users.json", "r") as file:
        temp_data = json.load(file)  
    return temp_data

def computeAge(temp_DOB):
    #If current month is before birth month, wrong age will be computed. MUST FIX!
    today = date.today()    
    temp_age = today.year - temp_DOB.year - ((today.month, today.day) < (temp_DOB.month, temp_DOB.day))
    setAge(temp_age)

def computeBMI(temp_weight, temp_height):
    temp_height = (int(temp_height) * int(temp_height))
    temp_BMI = (int(temp_weight) / temp_height) * 703
    setBMI(round(temp_BMI, 2))
    
def computeStatus(temp_BMI):
    #Have to add gender and age specification
    if temp_BMI >= 0 and temp_BMI <= 18.5:
        temp_status = "Underweight"
    if temp_BMI > 18.5 and temp_BMI <= 25:
        temp_status = "Healthy"
    if temp_BMI > 25 and temp_BMI <= 30:
        temp_status = "Overweight"
    if temp_BMI > 30:
        temp_status = "Obese"
    setStatus(temp_status)

def validateUser(temp_name):
    temp_data = []
    temp_data = getData()
    if temp_name in temp_data.keys():
        temp_boo = True
    else:
        temp_boo = False
    return temp_boo

def defineData(temp_name):
    temp_data = []
    temp_data = getData()
    setGender(temp_data[temp_name]["Gender"])
    setDOB(temp_data[temp_name]["Date of Birth"])
    setAge(temp_data[temp_name]["Age"])
    setWeight(temp_data[temp_name]["Weight"])
    setHeight(temp_data[temp_name]["Height"])
    setBMI(temp_data[temp_name]["BMI"])
    setStatus(temp_data[temp_name]["Status"])
    
def deleteData(temp_name):
    temp_data = []
    temp_data = getData()
    del temp_data[temp_name]
    writeUsers(temp_data)
    
def appendData(temp_name, temp_gender, temp_weight, temp_height):
    computeBMI(temp_weight, temp_height)
    temp_BMI = getBMI()
    computeStatus(temp_BMI)
    temp_data = []
    temp_data = getData()
    temp_data[temp_name]["Gender"] = temp_gender
    temp_data[temp_name]["Weight"] = temp_weight
    temp_data[temp_name]["Height"] = temp_height
    temp_data[temp_name]["BMI"] = temp_BMI
    temp_data[temp_name]["Status"] = getStatus()
    writeUsers(temp_data)
    defineData(temp_name)
    
def setData(temp_name, temp_gender, temp_DOB, temp_weight, temp_height):
    global name, gender, DOB, age, weight, height, BMI, status
    today = date.today()
    temp_month, temp_day, temp_year = temp_DOB.split("/")
    
    if int(temp_year) + 2000 > today.year:
        actual_year = int(temp_year) + 1900
    else:
        actual_year = int(temp_year) + 2000
    
    temp_DOB = temp_month + "/" + temp_day + "/" + str(actual_year)
    temp_age = computeAge(date(int(actual_year), int(temp_month), int(temp_day)))
    computeBMI(temp_height, temp_weight)
    temp_BMI = getBMI()
    computeStatus(temp_BMI)
    temp_status = getStatus()
    temp_data = getData()
    newUser = {
        "Gender": temp_gender,
        "Date of Birth": temp_DOB,
        "Age": temp_age,
        "Weight": temp_weight,
        "Height": temp_height,
        "BMI": temp_BMI,
        "Status": temp_status
    }
    
    setName(temp_name)
    setGender(temp_gender)
    setDOB(temp_DOB)
    setAge(temp_age)
    setWeight(temp_weight)
    setHeight(temp_height)
    setBMI(temp_BMI)
    setStatus(temp_status)
    temp_data[temp_name] = newUser
    writeUsers(temp_data)
