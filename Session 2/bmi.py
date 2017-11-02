h = int(input("Please enter your height in cm: "))
w = int(input("Please enter your weight in kg: "))

H = h / 100

BMI = w/(H * H)
print("Your Body Mass Index, BMI = ", BMI)

if BMI < 16:
    print("Severly Underweight")

elif BMI < 18.5:
    print("Underweight")

elif BMI < 25:
    print("Normal")

elif BMI < 30:
    print("Overweight")

else:
    print("Obese")
