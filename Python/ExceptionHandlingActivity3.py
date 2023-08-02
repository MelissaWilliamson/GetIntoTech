def CheckNameAge():
## Enter user inputs
    try:
        age = int(input('Enter Your Age'))
        name = input('Enter Your Name')
## IF statement checks the age is valid ie 0 or above
        if age <0:
## Value error message if the number is less than 0
            raise ValueError("Error! Age must be greater than 0")
## print the outcome
        print(age, name)
    except Exception as e:
        print("Error! Enter the correct characters for age and name")
## Opening the try block to raise an exception if there's an error
try:
## Calling the function defined above
    CheckNameAge()
except ValueError as e:
    print("Error"+str(e))








