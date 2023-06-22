##Basic String - Single and Multi line string.

someString = "Some String"

SomeString1 = """
First line
Some multine strings
Third line
"""

print(someString)
print(SomeString1)

## String character sequence position

print(someString[0])
print(someString[1])

## String Length - returns the length of a string.

print(len(someString))

print("")
print("")

## Loop over a string

for x in someString:
    print(x)

print("")
print("")

## Some string methods

number = 3
AString = '3'

print(number+int(AString))

## String to upper and lower case
print(someString.upper())
print(someString.lower())

print("")
print("")

## Type your full name seprated by commas into a string variable and print the upper case and lower case instances of the string
## print out the length of your names combined

fullname = 'melissa, williamson'

print(fullname)
print(fullname.upper())
print(fullname.lower())
print(len(fullname))

## string replacement - change melissa to amber

fullname='melissa, williamson'
print(fullname.replace('melissa', 'amber'))
print(fullname)

print("")

## Search a string - find a particular letter, name, number etc.

print(fullname.find('williamson'))
print('williamson' in fullname)
print('x' in fullname)

print("")

## Slicing - substring (picking out a starting character and end character - start index and end index.

print(fullname[0:5])

## Can slice from start to position - slice/get a substring from start to position.
## :4 beginning to the chosen point
## 5: from chosen point to the end

print(fullname[:4])
print(fullname[5:])


print("")

## strip to remove whitespcae from a string  - strip is everything, rstrip is right side white space, lstrip is left side whitespace.

fullname2 = ' melissa, williamson '
print(fullname2)
print(fullname2.strip())

## remove trailing whitespace
print(fullname2.rstrip())

## remove leading whitespace
print(fullname2.lstrip())

## concatenate strings
firstname = 'melissa'
lastname = 'williamson'

fullname3 = firstname+" "+lastname+" "+"test"
print(fullname3)

age = 35
message = 'I am '+str(age)+' years old'
print(message)

print("")

## format - place holders and argument

message1 = 'I am {} years old'
print(message1.format(age))

message2 = 'I am {} years old, and I like {}'
print(message1.format(age, 'python'))

print("")

## Endswith and startswith

message3 = 'welcome to python'
print(message3.startswith('welcome'))
print(message3.endswith('python'))

print(message3.startswith('n'))
print(message3.endswith('e'))

print("")

## Split a string into a list

message4 = "Welcome to Python's Coolness"
print(message4.split())

message4 = "Welcome to Python's Coolness"
splitlist = message4.split()

for x in splitlist:
    print(x)

fullname = 'melissa, williamson'
print(fullname.split())

fullname = 'melissa williamson'
splitlist1 = fullname.split()

for y in splitlist1:
    print(y)

print("")

## Escape characters -

message5 = "hello world, it is \"sunny\" today"
print(message5)

message6 = "hello world, it is \nsunny today"
print(message6)

print("")

## write python code that takes a string as input and counts the number of vowels (a e i o u) in the string.
vowels = "aeiouAEIOU"
count = 0
input_string = input("Give me an input ")
for char in input_string:
    if char in vowels:
        count += 1
print(count)

print("")

## write a python code that takes a string as input and returns the reverse of the string.
hello_world = 'hello world'
print(hello_world[::-1])

print("")

## write a python code that takes a string as input and counts the number of words in the string. ASSume that words are separated by space.
string = input('string here')
split_string = string.split()
print(len(split_string))



































