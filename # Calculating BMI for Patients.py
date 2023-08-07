# Calculating BMI for Patients

def bmi(weight, height):
    index = weight / (height * height)
    return index

# For your patient
patient_0 = bmi(79, 190)
print("You are underweight:", patient_0 < 20.1)