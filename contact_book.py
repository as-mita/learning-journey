import os


class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def to_line(self):
        return f"{self.name}|{self.phone}|{self.email}\n"

    @staticmethod
    def from_line(line):
        name, phone, email = line.strip().split("|")
        return Contact(name, phone, email)


class ContactBook:
    FILE = "contacts.txt"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                pass  # create empty file

    def add_contact(self, name, phone, email=""):
        if not phone.isnumeric():
            print("Phone number must contain only digits!")
            return

        contact = Contact(name, phone, email)
        with open(self.FILE, "a") as f:
            f.write(contact.to_line())

        print("Contact added successfully!")

    def list_contacts(self):
        with open(self.FILE, "r") as f:
            lines = f.readlines()

        if not lines:
            print("No contacts found.")
            return

        print("\n------ CONTACT LIST ------")
        for line in lines:
            c = Contact.from_line(line)
            print(f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}")

    def search_contact(self, keyword):
        with open(self.FILE, "r") as f:
            lines = f.readlines()

        results = [Contact.from_line(l) for l in lines if keyword.lower() in l.lower()]

        if not results:
            print("No matching contacts found.")
            return

        print("\n------ SEARCH RESULTS ------")
        for c in results:
            print(f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}")

    def delete_contact(self, name):
        with open(self.FILE, "r") as f:
            lines = f.readlines()

        new_lines = [l for l in lines if not l.lower().startswith(name.lower())]

        if len(new_lines) == len(lines):
            print("No contact found with that name.")
            return

        with open(self.FILE, "w") as f:
            f.writelines(new_lines)

        print("Contact deleted successfully!")

    def menu(self):
        while True:
            print("\n========== CONTACT BOOK ==========")
            print("1. Add Contact")
            print("2. View All Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("\nEnter choice: ")

            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email (optional): ")
                self.add_contact(name, phone, email)

            elif choice == "2":
                self.list_contacts()

            elif choice == "3":
                keyword = input("Search keyword: ")
                self.search_contact(keyword)

            elif choice == "4":
                name = input("Enter name to delete: ")
                self.delete_contact(name)

            elif choice == "5":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    book = ContactBook()
    book.menu()
