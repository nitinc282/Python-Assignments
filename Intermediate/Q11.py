def  map_function(color):
    result = list(map(list, color)) 
    return result



color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
a=map_function(color)

print(a)
