## From file name (Mods) import Class (Account)
from Mods import Account
from Person import Person
from DogClass import Dog
from DogClass import Bulldog

some_account=Account(1000.0)
some_account.deposit(1000.0)
some_account.deposit(500)
some_account.withdraw(200)
print(some_account.getbalance())

melissa=Account(500)
melissa.withdraw(100)
print(melissa.getbalance())

## Instances of the persons account
Melissa = Person("Melissa",35)
Melissa.getinformation()
print("Melissa's name is "+Melissa.name)

##base class/super class
mainDog=Dog("Effie")
print(mainDog.bark())

## derived class
bdog=Bulldog("Effie","Bulldog")
print(bdog.run())
