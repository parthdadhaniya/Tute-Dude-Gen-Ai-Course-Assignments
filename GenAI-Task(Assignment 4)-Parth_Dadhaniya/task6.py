# Task 6: Read File Safely with os.path.exists()
import os

filename = input("Enter filename to open: ")

if os.path.exists(filename):
    print(f"\nOpening {filename}:")
    file = open(filename, "r")
    print(file.read())
    file.close()
else:
    print("Error: File does not exist.")

