import time
import random
import string


# -------------------- common utils ----------------

# function to check if username exist in the accounts
def is_user_in_account(username):
    # Read from accounts text file
    accounts = open('./accounts.txt')
    # looping over the accounts and trying to match the provided username
    for account in accounts:
        # Let's extract username and password from each account
        # splitting the line by comma separator would give use username at index 0,
        # and password at index 1
        user_info = account.split()  # [username, password]

        # if username matches any account in "accounts" file
        if user_info[0] == username:
            # return with a boolean True
            return True
    # if we are out of the loop, it means we haven't found a username match
    return False


# function to check if account exists in the accounts file
def is_account_match(username, password):
    if len(password) < 8:
        print("Exiting program in 2 seconds.\n")
        time.sleep(2)
        quit()

    # Read from accounts text file
    accounts = open('./accounts.txt')
    # looping over the accounts and trying to match the provided password
    for account in accounts:
        # Let's extract username and password from each account
        # splitting the line by comma separator would give use username at index 0,
        # and password at index 1
        user_info = account.split()  # [username, password]
        # checking if password matches any account in "accounts" file
        if user_info[0] == username and user_info[1] == password:
            # return with a boolean True
            return True
    # if we are out of the loop, it means we haven't found a username match
    return False


# function to create random password of given length and given type
# This function takes no argument and generates a 8 character
# random string with a combination of letters, digits, and punctuation
def generate_random_string():
    return ''.join(random.choices(string.punctuation + string.digits + string.ascii_letters, k=8))


# function to save user info to accounts file and exit the program after 2 seconds
# this function takes username and password as two arguments and write that to the account.txt file
def write_to_file(username, password):
    # user wants to save the info in the file. We are appending at the end of the file
    accounts = open("./accounts.txt", 'a')
    accounts.write(username + " " + password + "\n")
    # close the file
    accounts.close()
    print("Info has been saved successfully! Exiting program in 2 seconds.\n")
    time.sleep(2)
    quit()


# utils end here-------------------------------------

# Our program --------------------------------------------------------
# This function accepts an argument, prompts from username and password
# and validates the username and password against text file.
def my_program(option):
    if option == "1":  # user has selected the login option
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        # If no username is found
        if not is_user_in_account(username):
            print("No username found in our accounts. Program will exit in 2 seconds!")
            # sleep for 2 seconds
            time.sleep(2)
            # exit the program
            quit()

        # At this point, the username has been found,
        # let's check for the password too.
        if not is_account_match(username, password):
            print("Incorrect password!. Program will exit in 2 seconds!")
            time.sleep(2)
            quit()

        # At this point, both username and password are found in the account
        # it means the user details were correct.
        print("Login Successful!!")
        print("Your account information is: Username: " + username + " Password is: " + password)
        print("Exiting program in 2 seconds")
        time.sleep(2)
        quit()

    # if selected option is "Register"
    elif option == "2":
        new_username = input("Please pick up a username of your choice: ")

        # let's ask the user if they want their own password or would like to generate one
        choice = input("Enter 1 for your own password.\nEnter 2 for generating a password.\n")

        if choice == "1":
            new_password = input("Please pick up a password. Min length should be 8 character \n")

            if len(new_password) < 8:
                print("Minimum password length should be 8 character\n.Please try again")
                time.sleep(2)
                quit()
            else:
                # provided password length requirement is met, let's proceed and ask the user if they wish to save
                # this to accounts.txt file
                write_to_file(new_username, new_password)

        elif choice == "2":
            # user wants us to generate the password for them
            random_generated_pass = generate_random_string()

            # Save this info to accounts.txt
            write_to_file(new_username, random_generated_pass)

        else:
            # user has picked up an unknown option. Exit the program.
            print("Unknown option selected. Please select 1 or 2 only. Exiting program in 2 seconds")
            time.sleep(2)
            quit()
    else:
        # user has selected option "3"
        admin_user = input("Please enter your username: ")
        admin_pass = input("Please enter your password: ")

        if admin_user == "admin" and admin_pass == "password":
            # Open the accounts file, loop over it and prints the account per line
            accounts = open('./accounts.txt')
            print("Username -- Password\n")
            print("---------------------\n")
            for account in accounts:
                user_info = account.split()
                print(user_info[0] + " -- " + user_info[1])

            print("Exiting program in 2 seconds \n")
            time.sleep(2)
            quit()
        else:
            # not valid credentials
            print("Please check your credentials and try again. Exiting program in 2 seconds");
            time.sleep(2)
            quit()

    # ---- End of our program--------------------------------------------


# This variable is to check if user has provided a valid option
is_valid_option = False

while True:
    # Accepts user input for picking up the option from the menu
    selected_option = input("Pick up an option:\n1.Login\n2.Register\n3.View Accounts\n4.Exit Program\n")

    if selected_option == "1" or selected_option == "2" or selected_option == "3":
        is_valid_option = True
        my_program(selected_option)

    elif selected_option == "4":
        # User wants to exit the program
        print("Exiting program in 2 seconds")
        time.sleep(2)
        break
    else:
        # user has entered an unknown option
        print("Unknown option! Please enter 1, 2 or 3!\n")
