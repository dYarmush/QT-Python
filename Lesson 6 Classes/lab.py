# 3. Create a Student class with the following :
# Data Members:
# - Name (string)
# - ID (string)
# - Grades (Array of 5 nums)
# Functions :
# -PrintAvg– will print the student’s grades avarage

class Student():
    def __init__(self,name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades
      
        #self.grades.append(grades)
    
    def add_grade(self,grade):
        
        if len(self.grades) < 5:
            self.grades.append(grade)
        else:
            print("no room left in grades")

    def printAvg(self):
        avg = 0
        for grade in self.grades:
            avg += grade
        print(f"{self.name}'s average is: "+ str(avg/len(self.grades)))

class School():
    def __init__(self,name, students):
        self.name = name
        self.students = students

    def add_student(self, student): 
        if isinstance(student, Student):   
            self.students.append(student)
    
    def print_avg(self):
        for student in self.students:
            student.printAvg()

s = Student("dovi",1, [1,2,3,4,5])
s2 = Student("adi",2,[2,4,6,8,10])
s3 = Student("dovi",1, [10,20,30,40,50])
s4 = Student("adi",2,[20,40,60,80,100])

school = School("test",[s,s2])
school.print_avg()
s.add_grade(6)
s.printAvg()

school2 = School("school2",[s3,s4])

#s.PrintAvg()

def school_Avg(schools):
    for school in schools:
        school.print_avg()

school_Avg([school,school2])

# 4*. Extend the Student c,lass in a way that he will get the maximum grades allowed in
# the constructor & add a function called AddGrades that will receive a grade and will add
# it to the array of grades as long as there is a free space. Otherwise – show a proper
# message

# 5.Create School class with the following :
# Data Members
# Name (string)
# Students ( an array of students)

# Functions
# AddStudent - will get a student object as a parameter and add it to the array
# PrintAvg – Will print all the students average,
# 6*. Create a function that receives an array of School objects and prints all their
# students averages.