
def get_even_length_strings(filename):
    even_length_strings = []

    with open(filename, "r") as file:

        content=(file.read())
        for i in content.split():
            if len(i)%2==0:
                even_length_strings.append(i)
        return even_length_strings

filename="D:\Study\ConsultAdd\Traning\docs.txt"
a=get_even_length_strings(filename)

print(' '.join(a))