Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency_count = {}

for item in Input_list:
    if (item in Frequency_count):
        Frequency_count[item]=Frequency_count[item]+1
    else:
        Frequency_count[item]=1
print(Frequency_count)
print(Frequency_count.keys)
print(Frequency_count.values)
a=Frequency_count.items()
print(a)