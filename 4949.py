strset = []
while(True):
    a = input()
    
    if a == ".":
        break
    
    strset.append(a)


for str in strset:
    
    stack = []
    isSatisfied = True
    
    for i in range(len(str)):
        if str[i] == "(":
            stack.append("(")
        
        if str[i] == "[":
            stack.append("[")
        
        if str[i] == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    isSatisfied = False
                    break
            else:
                    isSatisfied = False
                    break
            
            
        if str[i] == "]":
            if stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    isSatisfied = False
                    break
            else:
                    isSatisfied = False
                    break
                
    
    if isSatisfied and not stack:
        print("yes")
    else:
        print("no")