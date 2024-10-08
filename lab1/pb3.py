#Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def occurences(substring,string):
    return string.count(substring)

string=input("Input a string")
substring=input("Input a substring")

print(occurences(string,substring))