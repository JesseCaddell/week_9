def stringReverse(input):
    if len(input) == 0:
        return
    else:
        stringReverse(input[1:])

        print(input[0], end='')



stringReverse("hello")
    
