#12.Write a Python program to copy the contents of a file to another file.


def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Successfully copied contents from '{source_file}' to '{destination_file}'")
    except FileNotFoundError:
        print(f"Error: One of the files '{source_file}' or '{destination_file}' not found")
    except IOError:
        print(f"Error: Unable to read from '{source_file}' or write to '{destination_file}'")


source_file = 'textfile.txt'  
destination_file = 'Q7textfile.txt'  

copy_file(source_file, destination_file)
