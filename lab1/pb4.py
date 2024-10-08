#Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.



def uperCC_to_underscore(string):
    counter=0;
    modified_list=[] #caracterele si sirurile sunt imutabile
    for i in string:
        if i.isupper():
            if(counter==0):
                modified_list.append(i.lower())
                counter+=1
            else:
                modified_list.append('_')
                modified_list.append(i.lower())
        else:
            modified_list.append(i)
    modified_string=''.join(modified_list)
    return modified_string

print(uperCC_to_underscore("UpperCamelCase"))