from contacts_app import saveContactsFile, readContactsFile
from contact_class.contact_class import Contact

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