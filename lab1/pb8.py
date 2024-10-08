#Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

def num_of_words(string):
    s=string.split(' ')
    return len(s)

print(num_of_words("Ana are mere"))