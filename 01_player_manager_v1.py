"""
player manager
v1 - set up player management
"""
import csv  # Import the csv module to work with CSV file

# ask user to enter their name and store inout in the variable 'name'
name = input("Enter your name: ")

# ask user to enter their age and store the input in the variable 'age'
age = input("Enter your age: ")

# Open the 'user_data.csv' file in append mode ('a') so new data will be added to end of the file
# 'newline' is set to an empty string to ensure new lines are handled correctly across different platforms
with open('user_data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)  # Create a CSV writer object
    writer.writerow([name, age])  # Write a row with the entered name and age to the CSV file

# Print a confirmation message
print("Data saved successfully!")
