def JtoI(filename):

    with open(filename, 'r') as file: 
        content=(file.read())
    
        for i in content:
            c=i.replace("J","I")
            print(c, end="")

filename="D:\Study\ConsultAdd\Traning\words.txt"
JtoI(filename)


