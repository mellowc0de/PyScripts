# User inputs - Weight (pounds) and Height (inches)
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

# Calculation constants for kilograms per pound and meters per inch
KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

# Calculation for weight in kilograms
# Calculation for height in meters
# Calculation for bmi
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)


if bmi < 18.5:
  print("Result: Underweight")
elif bmi < 25:
  print("Result: Normal")
elif bmi < 30:
  print("Result: Overweight")
else:
  print("Result: Obese")
