#3.Write a Python program to append text to a file and display the text
def append_to_file(file_name, content):
    try:
        
        with open(file_name, 'a') as file:
            
            file.write(content)
        print(f"Content appended to '{file_name}' successfully.")

       
        display_appended_content(file_name)
    except Exception as e:
        print(f"Error: {e}")

def display_appended_content(file_name):
    try:
        
        with open(file_name, 'r') as file:
            
            appended_content = file.read()
            
            print(f"Appended Content:\n{appended_content}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"Error: {e}")


file_name = 'textfile.txt'
content_to_append = "\n Often, programmers fall in love with Python because of the increased productivity it provides. "

append_to_file(file_name, content_to_append)
