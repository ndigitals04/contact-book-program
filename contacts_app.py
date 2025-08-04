from contact_class.contact_class import Contact
from pathlib import Path
import ast
import sys
contacts_file_location = "C:/Users/NEW USER/Documents/python/contact-book/contacts.txt"


def instructions():
    print("Welcome to the Contact Book Application!")
    print("Please follow the instructions below for best results")
    print("- To create a new contact, type 'create'")
    print("- To view contacts or search for one, type 'view'")
    print("- To delete a contact, type 'delete' you can search for the contact's name using 'view'command")
    print("- To exit the application, type 'exit'")
    print("You can also type 'help' to see these instructions again.")

def readInput():
    while True:
        print("Please enter your command:")
        user_input = input()
        if user_input.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            sys.exit()
        elif user_input.lower() == 'help':
            instructions()
        elif user_input.lower() == 'create':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email (optional, leave blank if not available): ")
            address = input("Enter contact address (optional, leave blank if not available): ")
            contact = {"name":name,"phone": phone,"email": email,"address": address}
            return ("create", contact)
        
        elif user_input.lower() == 'view':
            search_term = input("Enter name or phone number to search for: ")
            search_results = Contact.view(None, contacts, search_term)
            if search_results[0] == "success":
                for contact in search_results[1]:
                    print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
            else:
                print(search_results[1])
            
        elif user_input.lower() == 'delete':
            name = input("Enter the name of the contact to delete(" \
            "you can use 'view' command to check the correct name): ")
            return ("delete",name)
            

        else:
            print("Invalid command. Please try again or type 'help' for instructions.")
            

def readContactsFile():
    file = Path(contacts_file_location)
    if file.exists():
        with open(file,"r") as file:
            file_text = file.read()
            return ast.literal_eval(file_text)
    else:
        with open(file, "w") as contacts_file:
            contacts_file.write("{}")
        with open(file, "r") as contacts_file:
            file_text = contacts_file.read()
            return ast.literal_eval(file_text)

def saveContactsFile(contacts):
    file = Path(contacts_file_location)
    with file.open("w") as file:
        file.write(str(contacts))

def main():
    user_input = readInput()
    if user_input[0] == "create":
        contact = Contact(contacts, user_input[1]["name"], user_input[1]["phone"], 
                          user_input[1]["email"], user_input[1]["address"])
        response = contact.create()
        if response[0] == "success":
            saveContactsFile(response[2])
            print(response[1])
        else:
            print(response[1])
    elif user_input[0]== "delete":
        response = Contact.find_by_name(None,contacts, user_input[1])
        if response[0]== "error":
            print(response[1])
        else:
            while True:
                print(f"Are you sure you want to delete the contact '{user_input[1]}'? (yes/no)")
                confirmation = input().lower()
                if confirmation == 'yes':
                    response = Contact.delete(None,contacts, user_input[1])
                    if response[0] == "success":
                        saveContactsFile(response[2])
                        print(response[1])
                    else:
                        print(response[1])
                    break
                elif confirmation == 'no':
                    print("Deletion cancelled.")
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
        
    main() # Recursively call main to continue the loop

contacts = readContactsFile()
instructions()
main()