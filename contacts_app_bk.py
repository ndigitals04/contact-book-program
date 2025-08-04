from contact_class.contact_class import Contact
from pathlib import Path
import ast
contacts_file_location = "C:/Users/NEW USER/Documents/python/contact-book/contacts.txt"

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

contacts = readContactsFile()
# test = Contact(contacts,name="James",phone="090880234668")
# test = test.create()
# if test[0] == "success":
#     contacts = test[2]
#     saveContactsFile(contacts)
#     print(test[1])
# else:
#     print(test[1])

# search_result = Contact.view(None,contacts, "Pet")
# if search_result[0] == "success":
#     for contact in search_result[1]:
#         print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
# else:
#     print(search_result[1])

response = Contact.delete(None,contacts, "James")
if response[0] == "success":
    saveContactsFile(response[2])
    print(response[1])
else:
    print("Error finding contact to delete.")