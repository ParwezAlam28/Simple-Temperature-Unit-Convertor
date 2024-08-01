# Project to convert celcius to fahrenheit and fahrenheit to celcius

import time

def c_to_f(): # Function to convert C to F
    c = float(input("\nEnter the temperature in °C: "))
    f =(9/5) * c + 32
    print(f"{c}°C ~ {round(f, 3)}°F")

def f_to_c(): # Function to convert F to C
    f = float(input("\nEnter the temperature in °F: "))
    c = (f-32)/9 * 5
    print(f"{f}°F ~ {round(c, 3)}°C")

# Creating Menu Screen using loop
while True:
    print("\n*** Temperature Unit Convertor ***")
    choice = int(input("\nPress 1 - Celsius to Fahrenheit\nPress 2 - Fahrenheit to Celsius\nPress 3 - Quit/Exit\n\nEnter your choice: "))

    if (choice<1) or (choice>3):
        print("\nInvalid choice, choose number between 1 - 3")
    elif choice==1:
        c_to_f()
    elif choice==2:
        f_to_c()
    elif choice==3:
        print("\nExiting the program\n")
        time.sleep(2)
        break