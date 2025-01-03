
# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
# This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.
print("BMI Calculator ")
weight = int(input("Enter your weight \n"))
height = float (input("Enter your height \n"))
bmi =  weight / height ** 2
print(f"BMI is {bmi}")