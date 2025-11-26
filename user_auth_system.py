import json
import os
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = hash_password(password)

    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash
        }


class UserAuthSystem:
    FILE = "users.json"

    def __init__(self):
        # Create file if not exists
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def load_users(self):
        with open(self.FILE, "r") as f:
            return json.load(f)

    def save_users(self, users):
        with open(self.FILE, "w") as f:
            json.dump(users, f, indent=4)

    def register(self, username, password):
        users = self.load_users()

        # Check if username exists
        for user in users:
            if user["username"].lower() == username.lower():
                print("❌ Username already exists.")
                return

        new_user = User(username, password)
        users.append(new_user.to_dict())
        self.save_users(users)
        print("✅ Registration Successful!")

    def login(self, username, password):
        users = self.load_users()
        hashed = hash_password(password)

        for user in users:
            if user["username"].lower() == username.lower():
                if user["password_hash"] == hashed:
                    print("✅ Login Successful!")
                    return True
                else:
                    print("❌ Incorrect password.")
                    return False

        print("❌ User not found.")
        return False

    def view_all_users(self):
        users = self.load_users()

        if not users:
            print("No users registered.")
            return

        print("\n------ Registered Users ------")
        for u in users:
            print(f"Username: {u['username']} | Password Hash: {u['password_hash']}")


def main():
    auth = UserAuthSystem()

    while True:
        print("\n========== USER AUTH SYSTEM ==========")
        print("1. Register")
        print("2. Login")
        print("3. View All Users (Admin)")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            auth.register(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            auth.login(username, password)

        elif choice == "3":
            auth.view_all_users()

        elif choice == "4":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
