#Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
from itertools import count


def how_many_bits(n):
    count = 0
    while n > 0:
        remainder = n % 2
        if(remainder == 1):
            count+=1
        n //= 2
    return count
print(how_many_bits(24))