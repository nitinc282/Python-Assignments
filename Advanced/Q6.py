n = int(input("Enter a Number : "))
list=[]
sum=0
for i in range (1,n):
    if n%i==0:
        list.append(i)

for j in list:
    sum=sum+j
#print("sum",sum)
if sum ==n:
    print("number is a perfect number")
else:
    print("number is not a perfect number")

