class Contact:   

    def __init__(self,contacts, name, phone, email=None, address=None):
        self.contacts = contacts
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    

    def create(self, contacts, name, phone, email=None, address=None):    
        contact_names = []
        for contact_name in contacts.keys():
            contact_names.append(contact_name)
        try:
            int(phone) # Ensure phone is numeric
        except ValueError:
            return ("error", "Invalid phone number format.")
        if name in contact_names:
            return ("error","Contact with this name already exists.")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        return ("success", f"Contact {name} created successfully.")

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
        return ("success", f"Contact {name} deleted successfully.")



    