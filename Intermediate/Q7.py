def find_median(numbers):
    numbers.sort()
    print(numbers)
    length=len(numbers)
    if length%2==1:
        return numbers[length//2]
    else:
        median1 = numbers[length // 2]
        median2 = numbers[length // 2 - 1]
        print(median1)
        print(median2)
        return (median1+median2)/2
        
numbers=[7, 2, 5, 1, 9, 3]
a=find_median(numbers)
print(f"The median is {a}")