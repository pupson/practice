date = input("Enter today's date: ")
rating = input("Rate your mood (1-10): ")
journal_entry = input("Input your thoughts for the day: ")

file = f"journal/{date}.txt"

with open(file, "w") as f:
    f.write(rating + 2*"\n")
    f.write(journal_entry)