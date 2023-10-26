import tkinter as tk
from tkinter import simpledialog, messagebox
from ttkthemes import ThemedStyle
import json

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.file_name = 'contacts.json'

        self.root = tk.Tk()
        self.root.title("Gestionnaire de Contacts")

        # Crée un objet ThemedStyle et applique le thème Breeze
        style = ThemedStyle(self.root)
        style.set_theme("breeze")

        # UI Elements
        self.nom_entry = tk.Entry(self.root, width=30)
        self.nom_entry.grid(row=0, column=1)
        tk.Label(self.root, text="Nom").grid(row=0, column=0)

        self.prenom_entry = tk.Entry(self.root, width=30)
        self.prenom_entry.grid(row=1, column=1)
        tk.Label(self.root, text="Prénom").grid(row=1, column=0)

        self.num_entry = tk.Entry(self.root, width=30)
        self.num_entry.grid(row=2, column=1)
        tk.Label(self.root, text="Numéro").grid(row=2, column=0)

        ajouter_button = tk.Button(self.root, text="Ajouter", command=self.ajouter_contact, width=25)
        ajouter_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2)
        self.listbox.bind('<Double-1>', self.on_listbox_double_click)

        supprimer_button = tk.Button(self.root, text="Supprimer", command=self.supprimer_contact, width=20)
        supprimer_button.grid(row=5, column=0, pady=5)
        modifier_button = tk.Button(self.root, text="Modifier", command=self.modifier_contact, width=20)
        modifier_button.grid(row=5, column=1, pady=5)

        self.load_contacts()

        self.root.mainloop()

    def ajouter_contact(self):
        nom = self.nom_entry.get()
        prenom = self.prenom_entry.get()
        num = self.num_entry.get()
        self.contacts.append({'nom': nom, 'prenom': prenom, 'num': num})
        self.refresh_listbox()
        self.save_contacts()

    def supprimer_contact(self):
        index = self.listbox.curselection()[0]
        del self.contacts[index]
        self.refresh_listbox()
        self.save_contacts()

    def modifier_contact(self):
        index = self.listbox.curselection()[0]
        nom = simpledialog.askstring("Modifier", "Entrez le nouveau nom", initialvalue=self.contacts[index]['nom'])
        prenom = simpledialog.askstring("Modifier", "Entrez le nouveau prénom", initialvalue=self.contacts[index]['prenom'])
        num = simpledialog.askstring("Modifier", "Entrez le nouveau numéro", initialvalue=self.contacts[index]['num'])
        if nom and prenom and num:
            self.contacts[index] = {'nom': nom, 'prenom': prenom, 'num': num}
            self.refresh_listbox()
            self.save_contacts()

    def on_listbox_double_click(self, event):
        index = self.listbox.curselection()[0]
        contact = self.contacts[index]
        messagebox.showinfo("Informations", f"Nom: {contact['nom']}\nPrénom: {contact['prenom']}\nNuméro: {contact['num']}")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['nom']} {contact['prenom']} - {contact['num']}")

    def save_contacts(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.contacts, file)

    def load_contacts(self):
        try:
            with open(self.file_name, 'r') as file:
                self.contacts = json.load(file)
                self.refresh_listbox()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    ContactManager()
