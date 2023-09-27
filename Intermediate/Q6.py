def is_power_of_two(n):
    # Base case: If n becomes 1, it's a power of two
    if n == 1:
        return True
    # Base case: If n becomes an odd number or less than 1, it's not a power of two
    elif n % 2 != 0 or n < 1:
        return False
    else:
        # Recursively check the result after dividing n by 2
        return is_power_of_two(n // 2)

# Test cases
num1 = 16
num2 = 12

if is_power_of_two(num1):
    print(f"{num1} is a power of two.")
else:
    print(f"{num1} is not a power of two.")

# if is_power_of_two(num2):
#     print(f"{num2} is a power of two.")
# else:
#     print(f"{num2} is not a power of two.")
