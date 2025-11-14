# bmi_calculator.py — Body Mass Index Calculator

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("⚠️ You are underweight.")
elif 18.5 <= bmi < 25:
    print("✅ You have a normal weight.")
elif 25 <= bmi < 30:
    print("⚠️ You are overweight.")
else:
    print("🚨 You are obese.")

