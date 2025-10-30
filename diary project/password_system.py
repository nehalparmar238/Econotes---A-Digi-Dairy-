import hashlib
import os

def set_password():
    print("Let's secure your diary with a password.")
    new_password = input("Set your password: ")
    h = hashlib.new("SHA256")
    h.update(new_password.encode())
    hashed_password = h.hexdigest()

    with open("password.txt", "w") as f:
        f.write(hashed_password)

    print("Password has been securely saved. Restart to log in.\n")

def verify_password():
    with open("password.txt", "r") as f:
        stored_hash = f.read().strip()

    print("Welcome back! Please enter your password to unlock your diary.")
    entered_password = input("Password: ")

    h = hashlib.new("SHA256")
    h.update(entered_password.encode())
    entered_hash = h.hexdigest()

    if entered_hash == stored_hash:
        print("Access granted! You can now write or read your notes.\n")
        return True
    else:
        print("Password incorrect! Please try again later.\n")
        return False
