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
    
def Peek(stk):
    if isEmpty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]
    
def Display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-top")
        for a in range (top-1,-1,-1):
            print(stk[a])

def PrintSalariesGreaterThan30K(stk):
    print("Employees with salary greater than 30000:")
    for item in stk:
        if item['SALARY'] > 30000:
            print(item['NAME'], "-", item['SALARY'])

#___main______
Stack=[]
top=None
while True:
    print("Menu for stack operation")
    print("1.push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display Stack")
    print("5.Greater")
    print("6.Exit")
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        name=input("Enter Your Name:")
        id=int(input("Enter ur id:"))
        desig=input('Enter Designation:')
        salary=int(input('Enter salary:'))
        item={'ID':id,'NAME':name,'DESIG':desig,'SALARY':salary}
        Push(Stack,item)
    elif ch==2:
        item=Pop(Stack)
        if item=="Underflow":
            print("Underflow!Stack is Empty!")
        else:
            print("Popped item is ",item)
    elif ch==3:
        item=Peek(Stack)
        if item=="underflow":
            print("Underflow! Stack is Empty")
        else:
            print("Topmost item is ",item)
    elif ch==4:
        Display(Stack)
    elif ch==5:
        PrintSalariesGreaterThan30K(Stack)

    elif ch==6:
        break
    else:
        print("Invalid Choice")
                      
