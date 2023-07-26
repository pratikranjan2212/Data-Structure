def isEmpty(Que):
    if Que==[]:
        return True
    else:
        return False
def Enqueue(Que,item):
    Que.append(item)
    if len(Que)==1:
        front=rear=0
    else:
        rear=len(Que)-1
        
def Dequeue(Que):
    if isEmpty(Que):
        return "Underflow"
    else:
        item=Que.pop(0)
        if len(Que)==0:
            front=rear=None
        return item
def Peek(Que):
    if isEmpty(Que):
        return "underflow"
    else:
        front=0
    return Que[front]
def Display(Que):
    if isEmpty(Que):
        print("Queue Empty!")
    elif len(Que)==1:
        print(Que[0],"<==front,rear")
    else:
        front=0
        rear=len(Que)-1
        print(Que[front],"<-front")
        for a in range (1,rear):
            print(Que[a])
        print(Que[rear],"<-rear")
#___main______
Queue=[]
front=None
while True:
    print("Menu for Queue operation")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.Display Queue")
    print("5.Exit")
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        item1=input("enter ur name")
        item2=int(input("Enter Roll No:"))

        item=[item1,item2]
        Enqueue(Queue,item)
       # input("Press Enter to continue")
    elif ch==2:
        item=Dequeue(Queue)
        if item=="Underflow":
            print("Underflow!Queue is Empty!")
        else:
            print("Dequeued item is ",item)
       # input("Press Enter to continue")    
    elif ch==3:
        item=Peek(Queue)
        if item=="underflow":
            print("Underflow! Queue is Empty")
        else:
            print("Frontmost item is ",item)
        input("Press Enter to continue")
    elif ch==4:
        Display(Queue)
        input("Press Enter to continue")
    elif ch==5:
        break
    else:
        print("Invalid Choice")
        input("Press Enter to continue")
                      
