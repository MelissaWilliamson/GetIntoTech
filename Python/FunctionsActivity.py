## pink
def area(width, height):
    area = width * height

print(area(20,15))
area(width=20,height=15)


print('')
print('')

## yellow

def oddOrEven(num):
    if num % 2 == 0:
        return print("even")
    else:
        return print('odd')
oddOrEven(num=6)

print('')
print('')

## black

#def freq(sent):
#    words = sent.split(' ')
#    counter = {i: words.count(i) for i in words}
#    for k, v in counter.items():
#       print(k, "appears", v, "times")
#def removesuffix():
#freq('Hello, my name name name is Hello Melissa')
#freq('Hello, my name name name is Hello Melissa'(str.removesuffix(',')))

def freq(sent):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punc = ""
    for x in sent:
        if x not in punc:
            no_punc = no_punc + x
    words = no_punc.split(' ')
    counter = {i: words.count(i) for i in words}
    for k, v in counter.items():
        print(k, "appears", v, "time(s)")
freq('Hello, my name!!!! name name:@ is Hello#][ Melissa')


