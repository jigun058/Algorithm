S = input()
S += " "
stack = []
isOpened = False

for i in range(len(S)):
    let = S[i]
    
    if isOpened:
        if let == ">":
            isOpened = False
            print(let, end="")
            continue
        else:
            print(let, end="")
            continue
    
    if let != " " and let != "<":
        stack.append(let)
    elif let == " ":
        while stack:
            print(stack.pop(), end="")
        print(" ", end="")
    elif let == "<":
        isOpened = True
        while stack:
            print(stack.pop(), end="")
        print("<", end="")