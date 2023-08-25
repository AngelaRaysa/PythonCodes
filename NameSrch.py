# Angela Raysa
# 11/10/2020
# NameSrch.py
# program to solve programming exercise 9.4

def main():
    #define variable
    SIZE = 10
    #array of names already sorted
    names = ['Ava Fischer', 'Bob White', 'Chris Rich', 'Danielle Porter',
             'Gordon Pike', 'Hannah Beauregard', 'Matt Hoyle', 'Ross Harrison',
             'Sasha Ricci', 'Xavier Adams']
    #variable to hold subscript of the name
    index = int()
    #variable to control the loop
    again = 'Y'
    while again == 'Y' or again == 'y':
        #get the name to search for
        searchName = input('Enter a name to search for: ')
        #search for the name
        index = binarySearch(names, searchName, SIZE)
        if index != -1:
            #display the prompt
            print('Congratulations! Name found!')
        else:
            #promt for another name
            print('Name not found ')
        again = input('Do you want to search again? (Y = Yes, N = No) ')
        
def binarySearch(array, value, arraySize):
    #variable to hold the subscript first element
    first = 0
    #variable to hold the subsript last element
    last = arraySize - 1
    #position of the search value
    position = -1
    #Flag
    found = False
    #variable to hold the subscript of the midpoint
    while not found and first <= last:
        #calculate the midpoint must be integer index
        middle = int((first + last) / 2)
        #see if the value is found at the midpoint
        if array[middle] == value:
            found = True
            position = middle
        #else if the value is in the lower half
        elif array[middle] > value:
            last = middle -1
        #else if the value is in the upper half
        else:
            first = middle +1
    #return the position of the item or -1
    #if the item was not found
    return position

#start program
main()

##Block comment to run program:
##Enter a name to search for: Angela Raysa
##Name not found 
##Do you want to search again? (Y = Yes, N = No) Y
##Enter a name to search for: Bob White
##Congratulations! Name found!
##Do you want to search again? (Y = Yes, N = No) 
