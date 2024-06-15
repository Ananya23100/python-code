# Specify the file names
source_file = "source.txt"
destination_file = "destination.txt"

try:
    # Open the source file in read mode
    with open(source_file, "r") as source:
        # Read the content of the source file
        content = source.read()

    # Open the destination file in write mode
    with open(destination_file, "w") as destination:
        # Write the content to the destination file
        destination.write(content)

    print(f"Content from {source_file} has been successfully copied to {destination_file}")

except FileNotFoundError:
    print(f"File '{source_file}' not found.")
except IOError:
    print(f"Error occurred while reading/writing file.")
