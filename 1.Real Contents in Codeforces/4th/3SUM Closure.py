import sys
test=int(sys.stdin.readline())
for line in range(test):
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    out=0
    for i in range(n-2):
        for j in range(i,n-1):
            if i!=j and (arr[i]-arr[j] == arr[j+1] or arr[i]-arr[j] ==- arr[j+1] ):
                for k in range(j,n):
                    if arr[i]+arr[j]+arr[k] not in arr and i!=j!=k:
                        print("NO")
                        out=1
                        break
            if out==1:
                break
        if out==1:
            break
    if out==0:
            print("YES")