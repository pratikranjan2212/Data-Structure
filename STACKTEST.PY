def push(thing):
    global top
    stack.append(thing)
    top=len(stack)-1

def peek():
    h=len(stack)-1
    print("\nThe value at the top",stack[h])

def display():
    p=len(stack)-1
    for i in range(p,-1,-1):
        print(stack[i],end=' ')

def  pop():
    global top
    if stack==[]:
        print("Underflow")
    else:
        if len(stack)==0:
            top=None
        else:
            top=top-1
        print("\nThe deleted item is ",stack.pop())

top=None
stack=[]
push(10)
push("abc")
push(30)
push(40)
push("soumya")
push(12)
display()
pop()
display()
pop()
peek()
display()
            
