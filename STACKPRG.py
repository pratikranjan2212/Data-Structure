# def isEmpty(stk):
#     if stk==[]:
#         return True
#     else:
#         return False
    
# def Push(stk,item):
#     stk.append(item)
#     top=len(stk)-1

# def Pop(stk):
#     if isEmpty(stk):
#         return "Underflow"
#     else:
#         item=stk.pop()
#         if len(stk)==0:              
#             top=None
#         else:
#             top=len(stk)-1
#         return item
    
# def Peek(stk):
#     if isEmpty(stk):
#         return "underflow"
#     else:
#         top=len(stk)-1
#         return stk[top]
    
# def Display(stk):
#     if isEmpty(stk):
#         print("Stack Empty")
#     else:
#         top=len(stk)-1
#         print(stk[top],"<-top")
#         for a in range (top-1,-1,-1):
#             print(stk[a])

# #___main______
# Stack=[]
# top=None
# while True:
#     print("Menu for stack operation")
#     print("1.push")
#     print("2.Pop")
#     print("3.Peek")
#     print("4.Display Stack")
#     print("5.Exit")
#     ch=int(input("Enter your choice(1-5):"))
#     if ch==1:
#         name=input("Enter Your Name:")
#         roll=int(input("Enter ur roll no"))
#         item=[name,roll]
#         Push(Stack,item)
#     elif ch==2:
#         item=Pop(Stack)
#         if item=="Underflow":
#             print("Underflow!Stack is Empty!")
#         else:
#             print("Popped item is ",item)
#     elif ch==3:
#         item=Peek(Stack)
#         if item=="underflow":
#             print("Underflow! Stack is Empty")
#         else:
#             print("Topmost item is ",item)
#     elif ch==4:
#         Display(Stack)
#     elif ch==5:
#         break
#     else:
#         print("Invalid Choice")

Only3_5=[]                      
def Push3_5(N):
    if N%3==0 or N%5==0:
        Only3_5.append(N)

NUM=[]
for i in range (5):
    n=int(input("Enter an integer:"))
    NUM.append(n)
    Push3_5(n)

while True:
    if len(Only3_5)==0:
        print("Empty Stack")
        break
    else:
        print(Only3_5.pop(),"",end='')

print(NUM)