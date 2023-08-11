# health-analytics
this is a primer assignment for HHA 504/507

## Summary
The first variable I created was:
```
temperature = float(input('Please Enter Your Current Body Temperature: '))
```
This was to ask the user to input their current body temperature. This is an example of a number (and float) variable. 

The next variable I created was:
```
name = input("Please Enter Your Name: ")
```
This was to ask the user to input their name. This is an example of a string variable.

I then went to put this:
```
print('Welcome back', name,',', 'from my observations:')
```
This is just a print function to welcome the user.

And this:
```
symptoms_experienced = ['shivering', 'shallow breathing', 'redness of the skin', 'excessive sweating']
```
This was just to show a list of symptoms that the patient may have experienced.

```
severity_of_the_symptom = {
    'shivering': 'mild for hypothermia',
    'shallow breathing': 'moderate for hypothermia',
    'redness of the skin': 'mild for hyperthermia',
    'excessive sweating': 'severe for hyperthermia'
    'none' : 'You\'re normal'
}
```
This was an example of a nested dictionary, which showed each of the symptoms and their severity (I only chose 4 but I can add more later on).

```
patient_information = {
    'Last Name First Name' : 'Zheng Helen',
    'Age' : 21,
    'Sex' : 'Female',
    'Symptoms' : ['fainting', 'excessive sweating', 'redness of the skin', 'hot skin']
}
```
This was just some background information about the patient. It is also a nested dictionary with a list in one of the key : value. 

```
temperature_ranges = {
    "normal" : (96.0, 99.0),
    "hypothermia" : (0.0, 95.0),
    "hyperthermia" : (100.4, 1000.0)
}
```
This is just to show the temperature ranges for each condition. This is a dictionary with strings, floats, and tuples.

```
if temperature < 96.0:
    print('You\'re not fine, you have hypothermia. Your current temperature is at: ', temperature)
elif 96 <= temperature <= 99.0:
    print('Hey, You\'re in normal range! Your current temperature is at: ', temperature)
else:
    print("You\'re not fine, you most likely have an infection or an illness. Please consult with your primary care physician. Your current temperature is at: ", temperature)
```
This portion is the function with if/else statements on testing if the patient's temperature is in range.

```
symptoms_experienced = input("symptoms_experienced: ")
```
This is another variable for the symptoms experienced by the patient. This will be used in the following if/else statement.

```
if symptoms_experienced == 'shivering':
    print(severity_of_the_symptom['shivering'])
elif symptoms_experienced == 'shallow breathing':
    print(severity_of_the_symptom['shallow breathing'])
elif symptoms_experienced == 'redness of the skin':
    print(severity_of_the_symptom['redness of the skin'])
elif symptoms_experienced == 'excessive sweating':
    print(severity_of_the_symptom['excessive sweating'])
elif symptoms_experienced == 'none':
    print(severity_of_the_symptom['none'])
else:
    print('Please consult your physician immediately')
```
This is another function with if/else statements on how severe the symptom the patient experienced is. 

## Expected Output
Because I made this a little more interactive, the expected outputs will be different depending on what the user enters.
For example if it was 98.6:
<img width="1000" alt="image" src="https://github.com/Helzheng123/health-analytics/assets/123939070/95394387-39c3-4a19-8fd6-30660438835d">

Now if I entered 94:
<img width="1000" alt="image" src="https://github.com/Helzheng123/health-analytics/assets/123939070/51de4ffb-5722-4398-b519-790cb7314e32">



