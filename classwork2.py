#1Given a set
s={10,20,30,40}
s.add(50)
print(s)

#2. Given a dictionary
student_grades={'Alice':98,'Bob':85,'charlie':74,'mike':70}
print(student_grades['charlie'])

#print all the student names in the given dictionary
student_grades['Bob']=90
print(student_grades)

#add a new item 'Sam':75 to the dictionary
student_grades['Sam']=75
print(student_grades)
#print the total number of students
print(len(student_grades))
#print all student names in the given dictionary
print(student_grades.keys())
#3.Given a dictionary
#
student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
                'Amal':{'maths':40,'science':45,'english':48,'history':43},
                'Anu':{'maths':45,'science':46,'english':47,'history':49}}

#print the mark of Amal in the subject History
print(student_marks['Amal']['history'])
#Update the mark of Arun in maths to 35
student_marks['Arun']['maths']=35
#print the marks of all students (in all subjects)
print(student_marks)