import re
from typing import Callable, Generator

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def greet():
    return "How can I help you?"

@input_error
def add_contact(args, contacts):
    username, phone = args
    contacts[username] = phone
    return "Contact added successfully."

@input_error
def change_contact(args, contacts):
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return "Phone number updated successfully."
    else:
        raise KeyError

@input_error
def get_phone(args, contacts):
    username = args[0]
    if username in contacts:
        return f"The phone number for {username} is {contacts[username]}."
    else:
        raise KeyError

@input_error
def get_all_contacts(contacts):
    if contacts:
        return "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    else:
        return "No contacts found."

def parse_input(command):
    parts = command.strip().lower().split(" ", 1)
    action = parts[0]
    args = parts[1].split() if len(parts) > 1 else []
    return action, args

def main():
    contacts = {}
    while True:
        command = input("Enter command: ")
        action, args = parse_input(command)
        
        if action == "hello":
            print(greet())
        elif action == "add":
            print(add_contact(args, contacts))
        elif action == "change":
            print(change_contact(args, contacts))
        elif action == "phone":
            print(get_phone(args, contacts))
        elif action == "all":
            print(get_all_contacts(contacts))
        elif action in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
