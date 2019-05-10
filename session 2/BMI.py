h = int(input("Enter your height in cm : "))
w = int(input("Enter your weight in kg : "))
BMI = w / ((h/100) ** 2)
print("Your BMI :",BMI)
if BMI < 16:
    print("You are serverely underweight")
elif 16 <= BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI < 25:
    print("You are normal")
elif 25 <= BMI < 30:
    print("You are overweight")
else:
    print("You are Obese")