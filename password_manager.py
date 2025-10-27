from cryptography.fernet import Fernet
import os




def write_key():
    """Generate and save a key if not exists."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """Load the existing key from key.key."""
    with open("key.key", "rb") as key_file:
        return key_file.read()


# Create key file if missing
if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)




def view():
    """View all saved passwords."""
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                data = line.rstrip()
                if "|" in data:
                    user, encrypted_pw = data.split("|")
                    decrypted_pw = fer.decrypt(encrypted_pw.encode()).decode()
                    print(f"User: {user}, Password: {decrypted_pw}")
    except FileNotFoundError:
        print("No passwords saved yet.")


def add():
    """Add a new account and password."""
    name = input("Account Name: ")
    pwd = input("Password: ")

    encrypted_pw = fer.encrypt(pwd.encode()).decode()

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted_pw + "\n")

    print(f"Password for {name} saved successfully!")




while True:
    mode = input(
        "\nWould you like to add a new password or view existing ones? (view, add), press 'q' to quit: ").lower()

    if mode == 'q':
        print("Goodbye 👋")
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode. Please type 'view', 'add', or 'q'.")
