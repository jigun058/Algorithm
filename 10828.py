stack = []

def push(x):
    stack.append(x)

def pop():
    if(len(stack)!=0):
        print(stack.pop())
    else:
        print("-1")

def size():
    print(len(stack))

def empty():
    if(len(stack)==0):
        print("1")
    else:
        print("0")

def top():
    if(len(stack)!=0):
        print(stack[len(stack)-1])
    else:
        print("-1")

N = int(input())

for i in range(N):
    mem = str(input())

    if(mem[1]=="u"):
        mem1, mem2 = mem.split()
        push(mem2)

    elif(mem == "pop"):
        pop()
    
    elif(mem == "size"):
        size()

    elif(mem == "empty"):
        empty()

    else:
        top()
