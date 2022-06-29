import sys
test=int(sys.stdin.readline())
for _ in range(test):
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    arr.sort()
    if len(arr)//2==0 :
        print(arr[int(n/2)-1])
    else :
        print(arr[int(n/2)])