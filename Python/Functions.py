##Functions##
##Define a function
def first_function():
    print("my very first python function")
    print("")

##Call the function
first_function()

##Passing arguments to functions

def second_function(first_name):
    print("my name is "+first_name)

second_function("Melissa")
second_function("Amber")

## Error appeared with this - due to argument not being supplied
##second_function()

def third_function(first_name,last_name):
    print("My full name is "+first_name+" "+last_name)

third_function("Melissa","Williamson")

## Error appeared with this - due to not having all the arguments supplied.
##third_function("Melissa")

## Unspecified number of parameters

def fourth_function(*params):
    print("the number of arguments is "+str(len(params))+" and the first in our argument list is "+params[0])

fourth_function("test")
fourth_function("test2","test")

def fifth_function(first_name, last_name):
    print("My full name is " + first_name + " " + last_name)

fifth_function(first_name="Melissa", last_name="Williamson")

## Multiple arguments with unspecified parameter names

def sixth_function(**params):
    print("The first argument is "+params["name"]+" and the second is "+params["name"])

sixth_function(name="Melissa", lname="Williamson")

## Default parameters

def seventh_function(age=35):
    print("my age is "+str(age))

seventh_function(30)
## Line 56 has used the default parameter where as 54 has used the parameter specified in the function call.
seventh_function()

print("")
print("")

## Functions accepting a list
ListOfcountries=["UK","GErmany","Spain","Italy"]

def countries_function(countries):
    print("there are "+str(len(countries))+" countries and their names are;")
    for x in countries:
        print(x)

countries_function(ListOfcountries)

print("")
print("")

## Functions using return keyword

def number(num):
    return num

print(number(5))
SomeNumber=number(5)
print(SomeNumber)

## Fucntions with empty body. Use pass keyword to avoid compiler errors.
def someFunction():
    pass

print("")
print("")

## Python recursion - A function calling itself
## Factorial of a number -

def factoria(num):
    if num==1:
        return 1
    else:
        return (num*factoria(num-1))

number=6
print("The factorial of "+str(number)+" is "+str(factoria(6)))

print('')
print('')

## Variable visibility in functions

result = 3

## result was the global variable so even though we wrote result = 42 the original result = 3 is printed.
def scope_test1():
    result = 42

scope_test1()
print(result)

## in this one we have overridden the global variable by stating 'global result' followed by result = 42
def scope_test2():
    global result
    result = 42

scope_test2()
print(result)





