
def get_lines_strings(filename):
    with open(filename, 'r') as file:  
	    lines = file.readlines()
        line_count = len(lines)
    return line_count

filename="D:\Study\ConsultAdd\Traning\demo.txt"
line_count=get_lines_strings(filename)
print(f"The number of lines in {filename} is: {line_count}")
