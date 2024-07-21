#8.Write a python program to find the longest words.

def find_longest_words(text):
    words = text.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words, max_length


example_text = """
hello, from python language.
"""

longest_words, max_length = find_longest_words(example_text)
print(f"The longest words in the text (length {max_length}) are:")
for word in longest_words:
    print(f"- {word}")
