#2.Write a Python program to read an entire text file.

def read_text_file(file_name):
    try:
       
        with open(file_name, 'r') as file:
            
            file_content = file.read()
            
            print(file_content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"Error: {e}")
file_name = 'textfile.txt'
read_text_file(file_name)

