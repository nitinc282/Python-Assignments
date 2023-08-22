def counts_vowels(string):
    vowels = "aeiouAEIOU"
    count=0
    for i in string:
        if i in vowels:
            count=count+1
    return count
    
    
string=input("enter the string:")
count=counts_vowels(string)
print(f"The no of vowel are {count}")
