def count_customers_without_computer(N, S):
    Costumer={}
    for i in range(0, len(S)):
        if i in S: #for in customer
            del i
        

# Example usage
N = 3
S = "GACCBDDBAGEE"
output = count_customers_without_computer(N, S)
print(output)  # Output should be 1
