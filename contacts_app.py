from contact_class.contact_class import Contact
from pathlib import Path
import ast
#

# test = Contact("Peter Ndukwe",)

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
