import os
from datetime import datetime

def write_entry():
    today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"\nNew Entry — {today}")
    entry = input("Write your diary entry: ")

    with open("diary.txt", "a") as f:
        f.write(f"\n\nDate: {today}\n{entry}\n")

    print("\nEntry saved successfully!\n")
