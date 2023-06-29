##string with an item/value
someString = ('Norwegian Blue')


## collection - list with items
fruitlist = ['banana','apples','guava','oranges']
numberlist = [3,5,7,9,1]

## Arithmetic opereations on lists
print('min',min(numberlist))
print('min',max(numberlist))
print('min',sum(numberlist))

print('')
print('')

## Access individual items using their indexes
print(numberlist[0])
print(numberlist[2])

## Length of a list (len)
print("length of the list is",len(numberlist))

## Return a range of items from a list
## Counting starts at 0 so 0 1 2 3 etc.
## start index inclusive and end index exclusive
## the value shown is the one prior to the end one
print(numberlist[1:3])

## Get items from beginning of list to a position
print(numberlist[:3])
print(numberlist[3:])

## Change items
numberlist[0]=90
numberlist[3:]=[50,50]

print(numberlist)

## Add items to a list

fruitlist+=['mangos','pineapple']
print(fruitlist)

## Remove items

fruitlist.remove('mangos')
print(fruitlist)

## iterate or loop over our list

for fruit in fruitlist:
    print(fruit)

## Occurance of an item in the list
count=fruitlist.count('pineapple')
print('mangoes occur',count,"time(s)")

## Find the index of an item
fruitlist.index('pineapple')

## Fidn the index of a non-existing item
##fruitlist.index('cars')

## Sort list items
fruitlist.sort()
print(fruitlist)
fruitlist.sort(reverse=True)
print(fruitlist)

## Dictionaries

mydict={'Australia':'Canberra','Eire':'Dublin','France':'Paris'}
print(mydict['Australia'])

country='Iceland'
mydict[country]='Reykjavik'
print(mydict['Iceland'])

print('')
print('')

## Dictionary sorting an object of type list
mydict2={'UK':['London','Wigan','Manchester'],'US':['Miami','New York','Boston']}
print(mydict2['UK'][2])

mydict2['FR']=['Paris','Lyon','Bordeaux']
print(mydict2['FR'][2])

for item in mydict2:
    print(mydict2[item])









