#  Creating a program that reads a file and writes a modified version to a new file.
# Open the file in read mode
with open('input.txt', 'r') as input_file:
    # Read the contents of the file
    content = input_file.read()

# Print the content to verify
print(content)

# Modify the content (example: convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open('output.txt', 'w') as output_file:
    output_file.write(modified_content)

# Print a confirmation message
print("Modified content written to 'output.txt'")
