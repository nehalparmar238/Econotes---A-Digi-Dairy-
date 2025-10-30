import os
from datetime import datetime

def read_note():
    print("\nDo you want to read today’s entry or a specific date?")
    choice = input("Type 'today' or enter a date (DD-MM-YYYY): ").strip()

    if choice.lower() == 'today':
        today_date = datetime.now().strftime("%d-%m-%Y")
        print(f"\nYour diary entries for today — {today_date}\n")

        if os.path.exists("diary.txt") and os.path.getsize("diary.txt") > 0:
            with open("diary.txt", "r") as f:
                entries = f.read()

            today_entries = [
                entry for entry in entries.split("\n\n")
                if f"Date: {today_date}" in entry
            ]

            if today_entries:
                print("\n\n".join(today_entries))
            else:
                print("No entries for today yet! Start writing one today ")
        else:
            print("No diary entries exist yet! Start writing your first one ")

    else:
        date_choice = choice
        print(f"\nYour diary entries for {date_choice}:\n")

        if os.path.exists("diary.txt") and os.path.getsize("diary.txt") > 0:
            with open("diary.txt", "r") as f:
                entries = f.read()

            date_entries = [
                entry for entry in entries.split("\n\n")
                if f"Date: {date_choice}" in entry
            ]

            if date_entries:
                print("\n\n".join(date_entries))
            else:
                print("No entries found for this date. Maybe write one today")
        else:
            print("No diary entries exist yet! Start writing your first one")
