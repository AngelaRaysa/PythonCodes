# Author:   Angela Raysa
# Date:     09/9/2020
# File:     ShipChg.py
# Descr:
# Homework activity to practice if then statements


# varible to hold real weight
realWt = float(input("Enter package weight: "))

# Define Main Function
def main():

# get a number from user and store it
    print("Enter package weight: ")
    
main()

# Define CalandDisplayShipping 

def CalcandDisplayShipping(): 

# set shipping charges 

    if realWt >= 11 : 
        realShp = 3.80
    if realWt <= 10 :
        realShp = 3.70
    if realWt <= 7 :  
        realShp = 2.20
    if realWt <= 2 :
        realShp = 1.10

# calculate and display shipping charges
    shipChg = float(realWt * realShp)

# Display shipping charges
    print("Shipping Charges: $", shipChg) 

CalcandDisplayShipping() 

 
