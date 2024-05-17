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
def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added successfully."

@input_error
def change_contact(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return "Phone number updated successfully."
    else:
        raise KeyError

@input_error
def get_phone(username, contacts):
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

def main():
    contacts = {}
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "hello":
            print(greet())
        elif command.startswith("add"):
            try:
                _, username, phone = command.split(" ", 2)
                print(add_contact(username, phone, contacts))
            except ValueError:
                print("Give me name and phone please.")
            except IndexError:
                print("Enter user name.")
        elif command.startswith("change"):
            try:
                _, username, phone = command.split(" ", 2)
                print(change_contact(username, phone, contacts))
            except ValueError:
                print("Give me name and phone please.")
            except IndexError:
                print("Enter user name.")
        elif command.startswith("phone"):
            try:
                _, username = command.split(" ", 1)
                print(get_phone(username, contacts))
            except ValueError:
                print("Give me name please.")
            except IndexError:
                print("Enter user name.")
        elif command == "all":
            print(get_all_contacts(contacts))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
