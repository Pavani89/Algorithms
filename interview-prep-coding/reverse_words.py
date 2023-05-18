'''
Challenge: Reverse Words in a Sentence
Write a Python function that takes a sentence as input and returns a new sentence with the words reversed.
'''

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Test the function
print(reverse_words("Hello, world!"))  # Output: olleH, dlrow!
print(reverse_words("Python is fun"))  # Output: nohtyP si nuf
