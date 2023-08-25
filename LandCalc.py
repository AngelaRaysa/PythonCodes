# Author:   Angela Raysa
# Date:     09/15/2020
# File:     LandArea.py
# Descr:
# Homework activity to calculate land area in acres

# constant to hold acres
ACRE = 43560

# variables to hold data
sqFt = float()
totAcre = float()

# prompt and read input
sqFt = int(input("Enter the square feet of land: "))

# perform calculations
totAcre = sqFt / ACRE

# display calculated result
print("The total acres are ", totAcre)

# sample program run:
# Enter the square feet of land: 23564
# The total acres are  0.5409550045913682
