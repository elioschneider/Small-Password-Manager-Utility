import random
import questionary
import time
import json

passwordList = []

try:
    with open("passwords.json", "r") as f:
        passwordList = json.load(f)
except FileNotFoundError:
    passwordList = []

def main():
    questionary.print("Passwort Utility")
    auswahl  = questionary.select(
    "Wähle eine Option:",
    choices=["generate new password", "password list", "exit"  ]
).ask() 
    match auswahl:
        case "generate new password":
            generate_password()
        case "password list":
            list_password_list()
        case "set new admin password":
            pass
        case "exit":
            print("exiting...")
            time.sleep(0.5)
            print("exited successfully")
            exit()

def generate_password():
    length = 0
    newPassword = ""
    rdigit = "" #random digit
    questionary.print("Passwort Generator")
    length = questionary.text("Password length?").ask()
    length = int(length)
    for i in range(length):
        rdigit = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
        newPassword = (newPassword + rdigit)
    questionary.print("Your password is: " + newPassword)
    time.sleep(1)
    save_to_list(password = newPassword)



def save_to_list(name = "None yet", password= "None yet"):
    answer= questionary.text("save password to list? (y/n)").ask()
    if answer == "y":
        name = questionary.text("what name do you want to save the password under?").ask()
        passwordList.append({"name": name, "password": password})
        with open("passwords.json", "w") as f:
            json.dump(passwordList, f, indent=4)
        print("Password saved.")
        time.sleep(0.5)
        main()
    elif answer == "n":
        print("Password not saved.")
        time.sleep(0.5)
        main()
    else:
        print("Invalid input.")
        time.sleep(0.5)
        save_to_list(password = password)


def list_password_list():
    for item in passwordList:
        print(f"Name: {item['name']}, Passwort: {item['password']}")
    exit_question()

def exit_question():
    exitvar = questionary.text("exit ? (y)").ask()
    if exitvar == "y":
        main()
    else:        
        print("Invalid input.")
        exit_question()

main()