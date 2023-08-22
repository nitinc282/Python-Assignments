def common_elements(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)

    return l3


l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

a=common_elements(l1,l2)
print(a)



