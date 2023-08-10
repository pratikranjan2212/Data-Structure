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
ch='yes'
while True:
    if ch=='yes':
        r=input("Enter Product Name:")
        k=int(input("Enter Price:"))
        item={r:k}
        if item[r]>=5000 and item[r]<=25000:
            Push(Stack,r)
        ch=input("Enter yes or no:")

    else:
        for i in Stack:
            print(i)
        print(Pop(Stack))
        break