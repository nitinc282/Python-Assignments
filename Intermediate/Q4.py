def rotate_array(arr, N, D):
    temp = arr[D:]  # Store the first D elements in a temporary array
    print(temp)
    a=[]
    # Shift the remaining elements to the right by D positions
    for i in range(1, N+1-D, 1):
        b=a.append(i)
    print(b)
        
    
    # Place the elements from the temporary array into the last D positions
    for i in range(D):
        arr[i] = temp[i]

# Example usage
arr = [1, 2, 3, 4, 5,6]
N = len(arr)
D = 2
rotate_array(arr, N, D)
print(arr)  # Output: [5,6, 1, 2, 3,4]
