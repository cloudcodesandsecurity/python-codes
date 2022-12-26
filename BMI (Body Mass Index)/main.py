print("Welcome to the BMI Calculator!\n")
print("Body Mass Index is a simple calculation using a person's height and weight. "
      "The formula is:\n BMI = kg/m2; Where kg is a person's weight in kilograms and m2 "
      "is their height in metres squared.\n Required: Measured - Weight and Height\n")

# Measured Weight and Height input 👇
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
print("Calculating...........................\n")


# BMI calculations and Result
bmi = round(weight / height **2)
if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese.")
else:
  print(f"Your bmi is {bmi}, you are clinically obese.")
