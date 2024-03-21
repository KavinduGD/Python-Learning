print("welcome to Python BMI console")
h=float(input("please enter your height - "))
w=float(input("please enter your weight - "))

bmi=w/(h*h)

if bmi < 18.5:
    print("undeer weight")
elif bmi < 25 and bmi>=18:
    print("normal weight")
elif  bmi < 30 and bmi>=25:
    print("slighlt overwight")
elif  bmi < 35 and bmi>=30:
    print("obese")
else:
    print("clinically obese")



