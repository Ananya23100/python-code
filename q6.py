# Define the file name
file_name = "output.txt"

# Read the content of the file and print it to the console
try:
    with open(file_name, "r") as file:
        content = file.read()
        print("The content of the file is:")
        print(content)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
