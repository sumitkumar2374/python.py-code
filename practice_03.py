# Write a program to print the contents of a directory using the os module . Search online for the function which does that .. 
import os

# Specify the directory path
path = input("Enter directory path: ")

try:
    # Get list of files and folders
    contents = os.listdir(path)

    print("\nContents of the directory:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
except Exception as e:
    print("Error:", e)
