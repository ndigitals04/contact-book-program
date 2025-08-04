from contact_class.contact_class import Contact
from pathlib import Path
import ast




def readContactsFile():
    file = Path("C:/Users/NEW USER/Documents/python/contact-book/contacts.txt")
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
        
contacts = readContactsFile()
test = Contact(contacts,name="Peter Ndukwe",phone="08012345678", email="peterking@234", address="No 1, Peter Street")
test = test.create()
if test[0] == "success":
    print(test[1])
else:
    print(test[1])