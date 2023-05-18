'''
Write a Python function that takes a sentence as input and returns a new sentence with the words in reverse order but the words itself are not reversed.
'''

def reverse_sentence(sentence):
    words = sentence.split()
    # print(words)
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Test the function
sentence = "Hello, world! This is a test."
result = reverse_sentence(sentence)
print(result)

