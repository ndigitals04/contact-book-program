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
test = Contact(contacts,name="James",phone="090880234668")
test = test.create()
if test[0] == "success":
    contacts = test[2]
    saveContactsFile(contacts)
    print(test[1])
else:
    print(test[1])