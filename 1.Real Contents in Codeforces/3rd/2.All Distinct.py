# problem Name :All Distinct
# Problem Link :https://codeforces.com/contest/1692/problem/B
# imput Operation
import sys
test=int(sys.stdin.readline())
for i in range(test):
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    arr.sort()
    iter=0
    for i in range(1,n) :
        if arr[i]==arr[i-1]:
            iter+=1
    if iter%2==0 :
        print(n-iter)
    elif iter%2==1 :
        print(n-iter-1)
