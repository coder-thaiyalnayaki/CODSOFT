import tkinter as tk
from tkinter import Label, Entry, Button, Listbox, Scrollbar, messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact

    def delete_contact(self, index):
        del self.contacts[index]

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contact_manager = ContactManager()

        # Labels and Entry widgets for contact details
        self.name_label = Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons for managing contacts
        self.add_button = Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.search_button = Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.update_button = Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # Listbox for displaying contact list
        self.contact_listbox = Listbox(root, width=50, height=10)
        self.contact_listbox.grid(row=0, column=2, rowspan=9, padx=10, pady=10)
        
        # Scrollbar for the contact listbox
        self.scrollbar = Scrollbar(root, orient="vertical")
        self.scrollbar.config(command=self.contact_listbox.yview)
        self.scrollbar.grid(row=0, column=3, rowspan=9, sticky="ns")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contact_manager.add_contact(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Name and phone are required.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contact_manager.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        keyword = simpledialog.askstring("Search Contact", "Enter name or phone:")
        if keyword:
            results = self.contact_manager.search_contact(keyword)
            if results:
                self.contact_listbox.delete(0, tk.END)
                for contact in results:
                    self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")
            else:
                messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search keyword.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_contact = self.contact_manager.contacts[selected_index]

            updated_name = simpledialog.askstring("Update Contact", "Enter updated name:", initialvalue=selected_contact.name)
            updated_phone = simpledialog.askstring("Update Contact", "Enter updated phone:", initialvalue=selected_contact.phone)
            updated_email = simpledialog.askstring("Update Contact", "Enter updated email:", initialvalue=selected_contact.email)
            updated_address = simpledialog.askstring("Update Contact", "Enter updated address:", initialvalue=selected_contact.address)

            if updated_name and updated_phone:
                updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
                self.contact_manager.update_contact(selected_index, updated_contact)
                messagebox.showinfo("Success", "Contact updated successfully.")
            else:
                messagebox.showwarning("Warning", "Name and phone are required.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
            if confirmation:
                selected_index = selected_index[0]
                self.contact_manager.delete_contact(selected_index)
                messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
