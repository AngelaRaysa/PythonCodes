# Author:   Angela Raysa
# Date:     09/28/2020
# File:     ifthen.py
# Descr:
# Homework activity to practice if then statements


# variables to hold data
amt1 = float()
amt2 = float()

#prompt and read input
amt1 = int(input("Enter a number: "))
amt2 = int(input("Enter another number: "))

#conditional statement
if amt1 > 10 and amt2 <100 :
    if amt1 > amt2 :
        print((amt1),"is the greater number")

    if amt2 > amt1 :
        print((amt2),"is the greater number")
    
# sample code
# Enter a number: 42
# Enter another number: 83
# 83 is the greater number
