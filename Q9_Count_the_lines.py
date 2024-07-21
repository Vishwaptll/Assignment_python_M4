#9.Write a Python program to count the number of lines in a text file

def count_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
    except IsADirectoryError:
        print(f"Error: '{file_name}' is a directory, not a regular file")
    except IOError:
        print(f"Error: Unable to read from file '{file_name}'")


file_name = 'textfile.txt'  
num_lines = count_lines(file_name)
if num_lines is not None:
    print(f"The total Number of lines in '{file_name}' is : {num_lines}")
