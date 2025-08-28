# File Read & Write Challenge 
# This program reads from one file and writes a modified version into a new file.

# Open the original file in read mode
with open("Newfile.txt", "r") as file:

# Read all lines from the file into a list
  lines = file.readlines()

# Modify each line: capitalize the first letter of each word
modified_lines = [line.title() for line in lines]

# Open the modified file in write mode
with open("Modified.txt", "w") as file:

# Write the modified lines to the New file
 file.writelines(modified_lines)

print("All lines of File has been read and modified content written to Modified.txt")


# 🧪 Error Handling Lab
# This program asks the user for a file name and tries to open it.
# If the file does not exist or cannot be opened, it shows a friendly error message.


# Prompt the user to enter a filename
filename = input("Enter the filename to read: ")

try:
    # Try to open the file in read mode
    with open(filename, "r") as file:
        # Display the contents of the file
        print(file.read())

# Handle case where file doesn't exist
except FileNotFoundError:
    print("Error: The file does not exist.")

# Handle case where file can't be accessed
except PermissionError:
    print("Error: You don't have permission to access this file.")

# Catch any other unexpected errors
except Exception as e:
    print(f"An unexpected error occurred: {e}")