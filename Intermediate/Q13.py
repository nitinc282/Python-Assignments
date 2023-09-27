

def string_starts(input_string,given_char):
    check = lambda input_string,given_char: True if (input_string[0] == given_char) else False
    result = check(input_string,given_char) #doubt why are we doing this
    if result==True:
        print(f"The string '{input_string}' starts with the character '{given_char}'.")
    else:
        print(f"The string '{input_string}' does not start with the character '{given_char}'.")

input_string = input("Enter a string:")
given_char = input("Enter a character:")     
string_starts(input_string,given_char)


