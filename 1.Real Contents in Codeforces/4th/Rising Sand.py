# Test Case wrong answer
import sys
test=int(sys.stdin.readline())
for line in range(test):
    n,k = map(int, input().split())
    arr=list(map(int, input().split()))
    count=0
    for i in range(0,n-2):
        if arr[i+1]>arr[i-1]+arr[i+2]:
            count+=1
        elif (k==2 or k==1) and i%2==0:
            count+=1
        # print(1)
    print(count)