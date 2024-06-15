# Prompt the user for input
user_input = input("Enter the string you want to write to the file: ")

# Define the file name
file_name = "output.txt"

# Write the input to the file
with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to {file_name}")
