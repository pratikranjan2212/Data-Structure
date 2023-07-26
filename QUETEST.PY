def Insert(N):
    global Front,Rear
    if(len(Queue)==1):
        Front=0
        Rear=0
    else:
        Rear=len(Queue)-1
    Queue.append(N)
    

def disp():
    if(len(Queue)==0):
        print("Underflow")

    else:
        print("The valuse is now")
        for i in range(0,len(Queue)):
            print(Queue[i],end=' ')
             
def dequeue():
    global Front,Rear
    if(len(Queue)==0):
        print("Underflow")
    else:
        if(len(Queue)==0):
            Front=None
            Rear=None
        else:
            Rear=Rear-1
        print("\n The value is deleted",Queue.pop(0))

def peek():
    print("\nThe value at the front inspected is ",Queue[0])
    
Front=None
Rear=None
Queue=[]
Insert(5)
Insert(7)
Insert(9)
disp()
peek()
dequeue()
dequeue()
disp()

