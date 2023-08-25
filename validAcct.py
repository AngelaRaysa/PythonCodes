# Angela Raysa
# 10/27/2020
# ValidAcct.py
# Program Excercise 8-5 to validate account numbers

# Define main module
def main():
    # Prompt and read input
    getUserAcct = int(input("Enter Account Number: "))
    
    # Declare variables and array
    validAcct = [5658845, 8080152, 1005231, 4520125, 4562555, 6545231, 7895122, 5552012, 3852085, 8777541, 5050552, 7576651, 8451277, 7825877, 1302850, 7881200, 1250255, 4581002]
    
    # Loop to validate values
    if getUserAcct in validAcct:
        print("This account is a valid account!")
    else:
        print("Invalid Account!")

# Call main module
main()