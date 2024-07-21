#11.Write a Python program to write a list to a file.
def write_list_to_file(file_name, lines):
    try:
        with open(file_name, 'w') as file:
            for line in lines:
                file.write(line + '\n')  
        print(f"Successfully wrote {len(lines)} lines to '{file_name}'")
    except IOError:
        print(f"Error: Unable to write to file '{file_name}'")


file_name = 'textfile.txt'  
lines_to_write = [
    "Thank you for reading this line 1.",
    "This is line 2.",
    "And here's line 3."
]

write_list_to_file(file_name, lines_to_write)
