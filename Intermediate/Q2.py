def unique_elements(l1):
    l2=[]
    for i in l1:
        if i in l2:
            continue
        else:
            l2.append(i)
    return l2

l1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5,6]


a=unique_elements(l1)
print(a) 