
def rotate_array(arr, D):
    N = len(arr)
    
    # Reverse the first N-D elements
    reverse(arr, 0, N - D - 1)
    
    
    # Reverse the remaining D elements
    reverse(arr, N - D, N - 1)
    
    # Reverse the entire array
    reverse(arr, 0, N - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Sample Input
arr = [1, 2, 3, 4, 5]
D = 2

# Rotate the array
rotate_array(arr, D)

# Print the rotated array
print("arr after rotation =", arr)
