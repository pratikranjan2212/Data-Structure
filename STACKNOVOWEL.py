NoVowel=[]
def PushNV(N):
    for i in range (len(N)):
        if 'A' in N[i] or 'E' in N[i] or 'I' in N[i] or 'O' in N[i] or 'U' in N[i]:
            pass
        elif 'a' in N[i] or 'e' in N[i] or 'i' in N[i] or 'o' in N[i] or 'u' in N[i]:
            pass
        else:
            NoVowel.append(N[i])

All=[]
for i in range(5):
    w=input("Enter words:")
    All.append(w)

PushNV(All)

while True:
    if len(NoVowel)==0:
        print("Empty Stack")
        break
    else:
        print(NoVowel.pop(),"",end='')