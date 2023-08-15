
Start = int(input("Enter the First Number : "))
Stop = int(input("Enter the Second Number: "))
Sum_of_odd_numbers=0

for i in range(Start+1,Stop):
    if i%2 !=0:
        Sum_of_odd_numbers=Sum_of_odd_numbers+i
        print(i)
print("Sum_of_odd_numbers",Sum_of_odd_numbers)

    
        
