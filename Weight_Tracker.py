from datetime import date 
import json
import csv
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
        - All of this information will be stored in a CSV file.  
"""
"""def setUser(firstName, lastName, gender, DOB, weight, height, BMI, status):
    dictionary = {
      "First Name": firstName,
      "Last Name": lastName,
      "Gender": gender,
      "Date of Birth": DOB,
      "Weight": weight,
      "Height": height,
      "BMI": BMI,
      "Status": status
    }
    json_object = json.dumps(dictionary, indent=4)
    with open("Users.json", "w") as file:
      file.write(json_object)"""

"""def setUser(firstName, lastName, gender, DOB, weight, height, BMI, status):
    user = [ [firstName, lastName, gender, DOB, weight, height, BMI, status]]
    with open("Users.csv", mode = "a") as file:
      csvwriter = csv.writer(file)
      csvwriter.writerow(user)"""
      
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
