#10.Write a Python program to count the frequency of words in a file

def count_word_frequency(file_name):
    word_freq = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word in word_freq:
                        word_freq[word] += 1
                    else:
                        word_freq[word] = 1
        return word_freq
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found")
    except IsADirectoryError:
        print(f"Error: '{file_name}' is a directory, not a regular file")
    except IOError:
        print(f"Error: Unable to read from file '{file_name}'")

file_name = 'textfile.txt'  
word_freq = count_word_frequency(file_name)

if word_freq is not None:
    print(f"Word frequency in '{file_name}':")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
