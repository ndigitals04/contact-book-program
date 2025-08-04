class Contact:   
    contacts = {}
    name = ""
    phone = ""
    email = None
    address = None

    def __init__(self,contacts, name, phone, email=None, address=None):
        self.contacts = contacts
        self.name = name.lower()
        self.phone = phone
        self.email = email
        self.address = address
    

    def create(self):    
        contact_names = []
        for contact_name in self.contacts.keys():
            contact_names.append(contact_name)
        try:
            int(self.phone) # Ensure phone is numeric
        except ValueError:
            return ("error", "Invalid phone number format.")
        if self.name in contact_names:
            return ("error","Contact with this name already exists.")
        self.contacts[self.name] = {"phone": self.phone, "email": self.email, "address": self.address}
        return ("success", f"Contact {self.name} created successfully.", self.contacts)

    def view(self,contacts,name_or_phone):
        search_results = []
        for name,value in contacts.items():
            if name_or_phone.isdigit():
                if name_or_phone in value["phone"]:
                    search_results.append([name, value["phone"], value.get("email", "N/A"), value.get("address", "N/A")])
            else:
                if name_or_phone in name:
                    search_results.append([name, value["phone"], value.get("email", "N/A"), value.get("address", "N/A")])
        
        return ("success", search_results) if search_results else ("not found", "No contacts found.")


    def delete(self,contacts, name):
        contacts.pop(name)
        return ("success", f"Contact {name} deleted successfully.", contacts)



    