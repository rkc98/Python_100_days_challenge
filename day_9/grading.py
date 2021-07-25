student_scores = {
  "Harry": 90,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  # print(student_scores[student])
  if(student_scores[student] in range(90,100)):
    student_grades[student]="outstanding"
  elif student_scores[student] in range(80,90):
    student_grades[student]="Exceeds expectation"
  elif student_scores[student] in range(70,80):
    student_grades[student]="Acceptable"
  else:
    student_grades[student]="failed"
# 🚨 Don't change the code below 👇
print(student_grades)
