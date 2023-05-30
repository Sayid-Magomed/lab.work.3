i = False
s = []
while i == False:
    inp = input()
    if inp == 'stop':
        i = True
    else:
        s.append(inp)

    print(" ".join(s))
