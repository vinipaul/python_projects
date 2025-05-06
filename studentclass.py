class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def showstudent_details(self):
        print(self.id,self.name,self.age)
stud1=Student(47,"vini",33)
stud1.showstudent_details()
class Person(Student):
    def __init__(self, id, name, age, languages) :
        self.language=languages
        super().__init__(id, name, age)
    def fulldetails(self):
        print("id=",self.id,"name=",self.name,"age=",self.age,"language=",self.language)
t1=Person(47,"vini",33,"hindi")
t1.fulldetails()