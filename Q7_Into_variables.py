#7.Write a Python program to read a file line by line store it into a variable.

def read_file_lines_into_variable(file_name):
    content = ""
    try:
        with open(file_name, 'r') as file:
            for line in file:
                content += line  
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
    except IsADirectoryError:
        print(f"Error: '{file_name}' is a directory, not a regular file")
    except IOError:
        print(f"Error: Unable to read from file '{file_name}'")
    return content

file_name = 'Q7textfile.txt'  
file_content = read_file_lines_into_variable(file_name)

print("Content read from file:")
print(file_content)

