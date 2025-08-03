class Contact:
    contacts= {}
    contact_names = []
    for contact_name in contacts.keys:
        contact_names.append(contact_name)
    

    def __init__(self, name, phone, email=None, address=None):
        try:
            int(phone) # Ensure phone is numeric
        except ValueError:
            return ("error", "Invalid phone number format.")
        if name in contact_names:
            return ("error","Contact with this name already exists.")
        contacts.append({name: {"phone": phone, "email": email, "address": address}})
        return ("success", f"Contact {name} created successfully.")

    def view(self,name_or_phone):
        search_results = []
        for contact in contacts:
            for name,value in contact.items():
                if name_or_phone.isdigit():
                    if name_or_phone in value["phone"]:
                        search_results.append([name, value["phone"], value.get("email", "N/A"), value.get("address", "N/A")])
                else:
                    if name_or_phone in name:
                        search_results.append([name, value["phone"], value.get("email", "N/A"), value.get("address", "N/A")])
        
        return ("success", search_results) if search_results else ("not found", "No contacts found.")


    def delete(self, name):
        for contact in contacts:
            contact_to_delete = contact.get(name)


    