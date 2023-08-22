string1 = input("Enter a string1 : ")
string2 = input("Enter a string2 : ")

# Sort both strings
str1 = sorted(string1)
str2 = sorted(string2)
print("str1",str1)
print("str2",str2)

if str1 == str2:
    print("equal")
else:
    print("not equal")