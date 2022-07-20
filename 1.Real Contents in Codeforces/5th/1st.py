import sys
t=int(sys.stdin.readline())
for i in range(t):
    a=[]
    n,m=map(int,sys.stdin.readline().split())
    a=list(map(int,sys.stdin.readline().split()))
    b=list("B"*m)
    # print(b)
    for j in range(n):
        x=min(m+1-a[j]-1,a[j]-1)
        if b[x]=="A":
            x=max(m+1-a[j]-1,a[j]-1)
        b[x]="A"
    print("".join(b))
