
def  encoded_string(s):

    for i in s:
        if i==0:

            parts= s.split()
            return parts
            
    first_name=parts[0]
    last_name=parts[1]
    id_values=parts[2]

            
    output={"first_name":first_name ,
            "last_name" : last_name,
            "id_values" : id_values }
            
    print(output)
s= "Robert000Smith000123"
encoded_string(s)

