#4.Write a Python program to read first n lines of a file.

def read_first_n_lines(file_name, n):
    try:
       
        with open(file_name, 'r') as file:
            
            lines = file.readlines()[:n]
            
            print(f"First {n} lines of '{file_name}':")
            for line in lines:
                print(line.rstrip())  
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"Error: {e}")


file_name = 'textfile.txt' 
n = 2  

read_first_n_lines(file_name, n)
