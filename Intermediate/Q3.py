def array_integer(n,k,l):
    Pair_count=0
    for i in range(0,len(n)):
        for j in range(i+1,len(n)):
            if n[i] + n[j]==k:
                Pair_count=Pair_count+1

    return Pair_count
n= [1, 2, 3, 4, 5]
k = 6
l=len(n)
a=array_integer(n,k,l)
print(a)