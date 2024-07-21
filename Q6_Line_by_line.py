#6.Write a Python program to read a file line by line and store it into a list

def read_file_lines(file_name):
    lines = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                lines.append(line.strip())  
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
    except IsADirectoryError:
        print(f"Error: '{file_name}' is a directory, not a regular file")
    except IOError:
        print(f"Error: Unable to read from file '{file_name}'")
    return lines

file_name = 'textfile.txt'  
lines = read_file_lines(file_name)
print("Lines read from file:")
for line in lines:
    print(line)
