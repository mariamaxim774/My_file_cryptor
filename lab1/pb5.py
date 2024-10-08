#write a function that validates if a number is a palindrome.

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("53135"))