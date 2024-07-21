#5.Write a Python program to read last n lines of a file

def read_last_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            for line in last_n_lines:
                print(line.rstrip())  
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
    except IOError:
        print(f"Error: Unable to read from file '{file_name}'")


file_name = 'textfile.txt'  
n = 1
read_last_n_lines(file_name, n)
