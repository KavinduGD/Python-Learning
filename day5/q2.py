student_heights=input("enter heights - ").split()



for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])



max=student_heights[0]

for height in student_heights:
    if max<height:
        max=height
        

print(f"max hight is {max}")
