def stringReverse(input):
    if len(input) == 0:
        return ""
    else:
        return stringReverse(input[1:]) + input[0]


reversed_string = stringReverse("hello")

print(reversed_string)
    
