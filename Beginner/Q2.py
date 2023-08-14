String = input("Enter a String: ")
Alpha_Count=0
Number_Count=0

for i in String:
    if i.isalpha():
        Alpha_Count=Alpha_Count+1
    elif i.isdigit():
        Number_Count=Number_Count+1

print( "Alphabets: ",Alpha_Count ,"& Number: ",Number_Count)

