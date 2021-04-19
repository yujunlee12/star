a=int(input("숫자 입력"))
d=a/2
d=int(d)
b=a
c=1
k=1
l=a
for i in range(a-d):
    for j in range((d+1)-(i+1)):
        print(" ",end='')
    for n in range(c):
        print("*",end='')
    print("")
    c=c+2
for m in range(a-(d+1)):
    for o in range(d-k):
        print(" ",end='')
    for p in range(5):
        print("*",end='')
    print("")
    k=k+1
    c=c-2
    
    
    
             
    
