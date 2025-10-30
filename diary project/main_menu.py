import os
from password_system import set_password, verify_password
from note_writer import write_entry as write_note
from note_reader import read_note

print("\nWelcome to Econotes - Your Digital Diary\n")


if os.path.exists("password.txt") and os.path.getsize("password.txt") > 0:
    if not verify_password():
        exit()
else:
    print("It looks like this is your first time here. Let's set a password!\n")
    set_password()

# --- Main Menu Loop ---
while True:
    print("\nMain Menu:")
    print("1. Write a new note")
    print("2. Read your notes")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == '1':
        write_note()
    elif choice == '2':
        read_note()
    elif choice == '3':
        print("\nGoodbye! See you soon!\n")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
