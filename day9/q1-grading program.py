student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

def grade(mark):
    if mark>90 :
        return "Outsanding"
    elif mark >80:
        return "Exceeds Expectations"
    elif mark > 70:
        return "Acceptable"
    else :
        return "Fail"
    

# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades={}


# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student_grades[key]=grade(student_scores[key])
    


# 🚨 Don't change the code below 👇
print(student_grades)