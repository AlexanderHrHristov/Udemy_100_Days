height = float(input("Enter your HEIGHT in centimeters:\n"))
weight = float(input("Enter your WEIGHT in kilograms:\n"))

bmi = weight / ((height/100) ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Your Weight is UNDERWEIGHT")

elif 18.5 >= bmi <= 25:
    print("Your Weight is NORMAL")

elif 25 > bmi <= 30:
    print("Your Weight is OVERWEIGHT")

elif 30 > bmi <= 35:
    print("Your are OBESE Class I")

elif 35 > bmi <= 40:
    print("Your are OBESE Class II")

elif bmi > 40:
    print("Your are OBESE Class III")