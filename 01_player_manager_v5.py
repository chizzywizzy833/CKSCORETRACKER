"""
player manager
v1 - set up player management
v2 - take version one and turn the code into a function, so it is easier to call
v3- add an option to view player data and turn into a function, so it is easier to call
v4- handling errors
v5 - deleting players
"""

import csv


def get_user_input():
    user_name = input("Enter your name: ").strip().capitalize()

    while True:
        user_age = input("Enter your age: ").strip()

        if not user_age.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        user_age = int(user_age)

        if user_age < 1 or user_age > 99:
            print("Please enter a number between 1 and 99.")
        else:
            break

    return user_name, user_age


def save_to_csv(_name, _age):
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([_name, _age])


def view_players():
    try:
        with open('user_data.csv', mode='r') as file:
            reader = csv.reader(file)
            users = list(reader)
            if not users:
                print("No users found.")
            else:
                print("Users:")
                for i, user in enumerate(users, 1):
                    if len(user) == 2:
                        print(f"{i}. {user[0]}, {user[1]}")
                    else:
                        print(f"Invalid data for user {i}.")
    except FileNotFoundError:
        print("No user data file found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def delete_player():
    """
    Delete a player from the CSV file based on the user's input.
    Displays the current list of players and prompts for the player number to delete.
    If the player number is valid, removes the player from the file.
    """
    try:
        with open('user_data.csv', mode='r') as file:
            reader = csv.reader(file)
            users = list(reader)

        if not users:
            print("No users to delete.")
            return

        print("Users:")
        for i, user in enumerate(users, 1):
            if len(user) == 2:  # Ensure there are exactly two columns
                print(f"{i}. {user[0]}, {user[1]}")
            else:
                print(f"Invalid data for user {i}.")

        while True:
            try:
                user_index = int(input("Enter the number of the player to delete: ").strip())
                if 1 <= user_index <= len(users):
                    del users[user_index - 1]  # Adjust for zero-based index
                    break
                else:
                    print("Invalid player number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        with open('user_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)

        print("Player deleted successfully!")

    except FileNotFoundError:
        print("No user data file found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Main Routine
name, age = get_user_input()
save_to_csv(name, age)
print("Data saved successfully!")

view_option = get_yes_no_input("Do you want to view players? (yes/no): ")
if view_option == "yes":
    view_players()

delete_option = get_yes_no_input("Do you want to delete a player? (yes/no): ")
if delete_option == "yes":
    delete_player()
