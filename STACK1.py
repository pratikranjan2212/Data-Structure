#WAP to append the following items using a list of stack
std=['ID','NAME','DESIG','MARK']
stk=[]

def Empty(stk):
    if stk==[]:
        return True
    else:
        return False
    
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1

def Pop(stk):
    if Empty(stk):
        return 'Underflow'
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
    
def Peek(stk):
    if Empty(stk):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]
    
def Display(stk):
    if Empty(stk):
        print('Stack Empty')
    else:
        top=len(stk)-1
        print(stk[top],'<-top')
        for a in range (top-1,-1,-1):
            print(stk[a])

#________main__________
Stack=[]
top=None
while True:
    print("Menu for stack operation")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display Stack")
    print("5.Exit")
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        name=input("Enter your name:")
        id=int(input("Enter id:"))
        desig=input('Enter Designation:')
        mark=int(input('Enter marks'))
        item=[name]