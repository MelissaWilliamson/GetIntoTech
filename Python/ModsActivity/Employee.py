class employee:

    def __init__(self, name):
        self.name = name

    def salary(self, salary):
        self.salary = salary

    def jobtitle(self, jobtitle):
        self.jobtitle = jobtitle

    def uplift(self, uplift):
        self.uplift = uplift

    def getInfo(self):
        print("The employee is called " + self.name)

    def salarychange(self, salarychange):
        self.salarychange = salarychange


