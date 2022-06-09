# Input Operations:
test=int(input())
for i in range(test):
    num=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    # Output Operation
    max=0
    for i in range(num):
        if a[i]-b[i]>max:
            max=a[i]-b[i]
    for i in range(num):
        a[i]-=max
        if a[i]<0:
            a[i]=0
    for i in range(num):
        if a[i]==b[i]:
            out=1
        else:
            out=0
            break
    if out==1:
        print("YES")
    else:
        print("NO")