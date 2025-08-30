'''
answer=""
for i in range(500):
    answer+=str(i)
    answer+="-"
#print(answer)

def send(sent):
    print(sent)

ll=len(answer)
if ll>200:
    a=ll//200
    b=ll%200
    for aa in range(a):
        sent=""
        for i in range(200):
            sent=sent+answer[i+aa*200]
        send(sent)
    sent=""
    for i in range(b):
        sent=sent+answer[a*200+i]
    send(sent)

print(ll,a,b)
'''
from time import localtime
t=localtime()
if t.tm_hour == 10 and t.tm_min == 29:
    print("666")
else:
    print("6")

def wtf():
    for i in range(5):
        if i!=3:
            continue
        else:
            return(i)