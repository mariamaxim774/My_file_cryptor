#Write a script that calculates how many vowels are in a string.
def number_of_vowels(s):
    counter=0
    for letter in s:
        for i in "AEIOUaeiou":
            if(letter==i):
                counter=counter+1;
    return counter
print(number_of_vowels("maria"))