def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
    
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1

def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk)==0:              
            top=None
        else:
            top=len(stk)-1
        return item

#_______main_______    
Stack=[]
top=None
while True:
    print("Menu for Stack of City")
    print("1.Push")
    print("2.Pop")
    print("3.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        c=input("Enter city name:")
        p=int(input("Enter pincode:"))
        item=[p,c]
        if item[1]=='Badodara':
            Push(Stack,item)
    if ch==2:
        item=Pop(Stack)
        print(item)
    if ch==3:
        break