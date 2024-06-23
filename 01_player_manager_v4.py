"""
player manager
v1 - set up player management
v2 - take version one and turn the code into a function, so it is easier to call
v3- add an option to view player data and turn into a function, so it is easier to call
v4- handling errors
"""
import csv


def get_user_input():
    """
    Get user input for name and age.
    Repeatedly prompts the user for age until a valid integer between 1 and 99 is entered.
    Ensures the first letter of the user's name is capitalised.
    """
    user_name = input("Enter your name: ").strip().capitalize()  # capitalise the first letter of the name

    while True:
        user_age = input("Enter your age: ").strip()

        # Check if the age is an integer
        if not user_age.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        user_age = int(user_age)

        # Check if the age is within the valid range
        if user_age < 1 or user_age > 99:
            print("Please enter a number between 1 and 99.")
        else:
            break

    return user_name, user_age


def save_to_csv(_name, _age):
    """
    Append the user's name and age to a CSV file.
    """
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([_name, _age])


def view_players():
    """
    Read and display user data from the CSV file.
    If no users are found or if the file doesn't exist, print an appropriate message.
    """
    try:
        with open('user_data.csv', mode='r') as file:
            reader = csv.reader(file)
            users = list(reader)
            if not users:
                print("No users found.")
            else:
                print("Users:")
                for i, user in enumerate(users, 1):
                    if len(user) == 2:  # Ensure there are exactly two columns
                        if i > 1:  # Skip printing the header
                            print(f"{i - 1}. {user[0]}, {user[1]}")  # Adjust numbering and exclude the header
                    else:
                        print(f"Invalid data for user {i}.")
    except FileNotFoundError:
        print("No user data file found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_yes_no_input(prompt):
    """
    Prompt the user for a yes/no response.
    Repeatedly prompts the user until a valid response ('yes' or 'no') is entered.
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Main Routine
name, age = get_user_input()
save_to_csv(name, age)
print("Data saved successfully!")

view_option = get_yes_no_input("Do you want to view players? (yes/no): ")
if view_option == "yes":
    view_players()
