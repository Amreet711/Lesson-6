height=float(input("How tall are you in metres?"))
weight=float(input("How much do you weigh in kilograms?"))
BMI=weight/height**2
print("Your BMI is",BMI)
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=29.9:
    print("You are overweight")
else:
    print("You are obeese")