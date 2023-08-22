def IndexError_exception(list,Index):
    try:
        result=list[Index]**2
        return result
    except IndexError:
        print("IndexError exception")
        return None



list=[1,2,3,4,5]

try:
    Index=int(input("enter an Index"))
    result=IndexError_exception(list,Index)
    if result is not None:
        print(f"The result of the operation is: {result}")

except:
    print("Invalid index input. Please enter a valid integer.")











Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
