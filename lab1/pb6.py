

def extract_number(string):
    number = 0
    found_number = False
    for i in range(0,len(string)) :
            if string[i].isdigit():
                j=i
                while j < len(string) and string[j].isdigit():
                    number=number*10+int(string[j])
                    j=j+1
                found_number=True
                break
    if found_number:
        return number
    else:
        return "nu exista un numar"
print(extract_number("buna"))