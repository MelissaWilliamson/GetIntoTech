class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print("woof")

    def run(self):
        print(self.name+"is running")

class Bulldog(Dog):
        def __init__(self,name):
            super().__init__(name)
        ## self.breed = bulldog
            self.breed = breed

        def bark(self):
            print("wooo")

        def stroke(self):
            print("stroking"+self.name)
