"""
player manager
v1 - set up player management
v2 - take version one and turn the code into a function, so it is easier to call
"""
import csv


def get_user_input():  # Make a function, so it is easier to call in main routine
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    return user_name, user_age


def save_to_csv(_name, _age):  # function
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age])


# Main routine

name, age = get_user_input()  # Get the player name and age from the user and store them in variables 'name' and 'age'
save_to_csv(name, age)  # Save the players name and age to the CSV file using the 'save_to_csv' function
print("Data saved successfully!")
