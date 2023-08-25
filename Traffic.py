# Author:  Angela Raysa
# Date:    11/4/2020
# Program: Traffic.py
# Descr:   Program to solve Unit 8 assignment


def program():
    num_days = 0
    max_cars = 0
    #accumulator
    sum_cars = 0
    avg_cars_per_day = 0
    file_name = input("Type the name of the data file : ")
    #file_name = "MainAndState.dat"
    #open file for reading
    f = open(file_name, "r")
    #counter to count the number of lines in the file
    counter = 0
    for line in f:
        counter += 1
        num_cars = int(line)
        sum_cars += num_cars
        if (num_cars > max_cars):
            max_cars = num_cars
    #close file
    f.close()
    num_days = counter
    avg_cars_per_day = sum_cars/num_days
    #print output
    print("Number of days monitored at the intersection :",num_days)
    print("Maximum number of cars passing through the intersection on a tracked day :",max_cars)
    print("Average cars per day passing through the intersection :",avg_cars_per_day)





program()


##Block comment to test program:
##Type the name of the data file : MainAndState.dat
##Number of days monitored at the intersection : 320
##Maximum number of cars passing through the intersection on a tracked day : 1998
##Average cars per day passing through the intersection : 1018.725
