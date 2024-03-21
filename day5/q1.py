student_heights=input("enter heights - ").split()



for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])



totla_height=0
num_student=0

for height in student_heights:
    totla_height=totla_height+height
    num_student=num_student+1
    
print(f"total_height - {totla_height}" )
print(f"total_student - {num_student}")
print(f"avg_height - {totla_height/num_student}" )
