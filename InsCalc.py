# Author:   Angela Raysa
# Date:     09/22/2020
# File:     InsCalc.py
# Descr:
# Homework activity to create a module to calculate minimum insurance

# Define insCalc function
def insCalc():
    
# constant to hold insurance
   INS = .80

# variables to hold data
   propValue = float()
   minIns = float()

# prompt and read input
   propValue = int(input("Enter the value of your property: $ "))

# perform calculations
   minIns = propValue * INS

# display calculated result
   print("Your minimum insurance amount is $", minIns)


# Call insCalc function
insCalc()
