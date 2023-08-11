import pandas as pd
import numpy as np

# We will now be testing temperature (in Fahrenheit) of patient Helen Zheng

temperature = float(input('Please Enter Your Current Body Temperature: '))

name = input("Please Enter Your Name: ")

print('Welcome back', name,',', 'from my observations:')

symptoms_experienced = ['shivering', 'shallow breathing', 'redness of the skin', 'excessive sweating']

# This is to show how severe the symptoms are:
severity_of_the_symptom = {
    'shivering': 'mild for hypothermia',
    'shallow breathing': 'moderate for hypothermia',
    'redness of the skin': 'mild for hyperthermia',
    'excessive sweating': 'severe for hyperthermia'
}
# mild just indicates the first sign/encounter

# Just background information about the patient
patient_information = {
    'Last Name First Name' : 'Zheng Helen',
    'Age' : 21,
    'Sex' : 'Female',
    'Symptoms' : ['fainting', 'excessive sweating', 'redness of the skin', 'hot skin']
}

# The following are temperature ranges for the normal body temperature in degrees Fahrenheit
temperature_ranges = {
    "normal" : (96.0, 99.0),
    "hypothermia" : (0.0, 95.0),
    "hyperthermia" : (100.4, 1000.0)
}

# Now we will test if the patient's temperature is in range

if temperature < 96.0:
    print('You\'re not fine, you have hypothermia. Your current temperature is at: ', temperature)
elif 96 <= temperature <= 99.0:
    print('Hey, You\'re in normal range! Your current temperature is at: ', temperature)
else:
    print("You\'re not fine, you most likely have an infection or an illness. Please consult with your primary care physician. Your current temperature is at: ", temperature)

# To check how severe the symptom is we will ask about the symptoms experienced; there are only a few listed here. 
   
symptoms_experienced = input("symptoms_experienced: ")

if symptoms_experienced == 'shivering':
    print(severity_of_the_symptom['shivering'])
elif symptoms_experienced == 'shallow breathing':
    print(severity_of_the_symptom['shallow breathing'])
elif symptoms_experienced == 'redness of the skin':
    print(severity_of_the_symptom['redness of the skin'])
elif symptoms_experienced == 'excessive sweating':
    print(severity_of_the_symptom['excessive sweating'])
else:
    print('Please consult your physician immediately')