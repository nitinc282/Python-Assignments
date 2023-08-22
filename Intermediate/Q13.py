

def string_starts(input_string,given_char):

    return lambda input_string,given_char : input_string.startswith("given_char")
       

input_string = input("Enter a string: ")
given_char = input("Enter a character: ")
result = string_starts(input_string,given_char)


if result :
    print(f"The string '{input_string}' starts with the character '{given_char}'.")
else:
    print(f"The string '{input_string}' does not start with the character '{given_char}'.")



