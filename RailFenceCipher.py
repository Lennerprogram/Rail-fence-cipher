def RailFence(rail, string):
    #variable creation
    a = []
    togetherlist = []
    line = 0
    column = 0
    increment = True

    #transform string to list
    string_split = list(string)

    #matrix creation
    for c in range(rail):
        a.append( ['|'] * len(string))

    #placement of values
    while True:
        if rail - line == 1:
            increment = False
        elif line == 0:
            increment = True

        a[line] [column] = string_split[column]
        
        if increment:
            line += 1
        else:
            line -= 1

        if column == len(string) - 1:
            break

        column += 1

    #output
    for i in a:
        print(i)

    #encrypted
    for c in range(rail):
        while a[c].count('|') > 0:
            a[c].remove('|')

    for c in range(rail):
        togetherlist += a[c]

    encrypted= ''.join(togetherlist)

    print(encrypted)
    return encrypted