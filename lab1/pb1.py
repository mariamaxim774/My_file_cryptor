print("hello")
#Find The greatest common divisor of multiple numbers read from the console.

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def gcd_multiple_numbers(*list_of_numbers):
    if(len(list_of_numbers)==0):
        return None

    gcd_total = list_of_numbers[0]
    for num in list_of_numbers[1:]:#incepe dupa primul element
        gcd_total=gcd(gcd_total,num)
    return gcd_total

numbers=[]
n=int(input("Cate numere vrei sa introduci?"))
for i in range(1,n+1):
    numar=int(input(f"Introduceti numarul {i+1}:"))
    numbers.append(numar)
result=gcd_multiple_numbers(*numbers)

print("Rezultatul este:",result)


