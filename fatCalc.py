# Author:   Angela Raysa
# Date:     09/22/2020
# File:     FatCalc.py
# Descr:
# Homework activity to create a module to calculate minimum insurance

def calcFat():
    fatG = int(input("Enter fat grams consumed in one day:"))
    global fatCal
    fatCal = float()
    fatCal = fatG * 9
    print("Calories from fat is:", fatCal)
calcFat()

def calcCarb():
    carbG = int(input("Enter carbohydrate grams consumed in one day:"))
    global carbCal
    carbCal= float()
    carbCal = carbG * 4
    print("Calories from carbohydrates is:", carbCal)
calcCarb()

def calcTot():
    global totCal
    totCal = float()
    totCal = carbCal + fatCal
    print("Total calories from fat and carbohydrates is:", totCal)
calcTot()
    
