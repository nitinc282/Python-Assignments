Number1 = int(input("Enter a number1 : "))
Number2 = int(input("Enter a number2 : "))

list1=[]
list2=[]
list3=[]
result=1

for i in range(2,Number1):
    n = Number1/i 
    if n==int(n):
        list1.append(i)
print(list1)
for j in range(2,Number2):
    m = Number2/j
    if m==int(m):
        list2.append(j)
print(list2)


for i in list1:
    if i not in list2:
        list3.append(i)
for i in list2:
    if i not in list1:
        list3.append(i)

for x in list3:
    result = result * x
print(result)


