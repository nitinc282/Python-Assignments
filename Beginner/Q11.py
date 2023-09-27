# 1 way
s=str(123)
def sum_of_digits(s):
    
    for i in range(len(s)):
        sum=0
        if len(s)!=1:
            for i in s: 
                sum = sum + int(i)
            s=str(sum)
        else:
            break 
    return s
a=sum_of_digits(s)
print(a)


#2nd way
n = 4567 

s_n = str(n)


while len(s_n) > 1:
    sum = 0
    for i in s_n:
        sum = sum + int(i)

    s_n = str(sum)#24
print(s_n)

