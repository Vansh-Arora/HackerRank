class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, fname, lname, idno, scores):
        Person.__init__(self,fname,lname,idno)
        self.scores = scores

    def calculate(self):
        avg = 0
        for i in self.scores:
            avg += i
        avg = avg//len(scores)
        if avg in range(90,101):
            return 'O'
        elif avg in range(80,90):
            return 'E'
        elif avg in range(70,80):
            return 'A'
        elif avg in range(55,70):
            return 'P'
        elif avg in range(40,55):
            return 'D'
        elif avg in range(1,40):
            return 'T'
        else:
            return 'Output will be correct only for right input'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())