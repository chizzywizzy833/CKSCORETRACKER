"""
player manager
v1 - set up player management
v2 - take version one and turn the code into a function, so it is easier to call
v3- add an option to view player data and turn into a function, so it is easier to call
"""
import csv


def get_user_input():
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    return user_name, user_age


def save_to_csv(_name, _age):
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([_name, _age])


def view_players():  # Define a function named view_players, which will make it easier to call this routine from
    # other parts of the program
    try:  # Start a try block to handle exceptions that may occur during file operations
        with open('user_data.csv', mode='r') as file:  # Open the file 'user_data.csv' in read mode
            reader = csv.reader(file)  # Create a CSV reader object to parse the file
            users = list(reader)  # Convert the parsed CSV data into a list of rows
            if not users:  # Check if the list of users is empty
                print("No users found.")  # Print a message indicating that no users were found
            else:  # If the list of users is not empty
                print("Users:")  # Print a header for the user list
                for i, user in enumerate(users, 1):  # Loop through the list of users with an index starting from 1
                    if len(user) == 2:  # Ensure that each row has exactly two columns
                        if i > 1:  # Skip printing the first row (assumed to be the header)
                            print(f"{i - 1}. {user[0]}, {user[1]}")  # Print the user information with adjusted
                            # numbering
                    else:  # If a row does not have exactly two columns
                        print(f"Invalid data for user {i}.")  # Print a message indicating that the row has invalid data
    except FileNotFoundError:  # Handle the case where the file 'user_data.csv' does not exist
        print("No user data file found.")  # Print an error message indicating the file was not found
    except Exception as e:  # Handle any other exceptions that might occur
        print(f"An error occurred: {str(e)}")  # Print a generic error message with the exception details


# Main Routine

name, age = get_user_input()
save_to_csv(name, age)
print("Data saved successfully!")

view_option = input("Do you want to view players? (yes/no): ")  # Prompt the user with a question and store their input
# in the variable view_option
if view_option.lower() == "yes":  # Check if the user's input, converted to lowercase, is equal to "yes"
    view_players()  # If the condition is met (the user inputted "yes"), call the view_players() function to display
    # the list of players
