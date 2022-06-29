# Problem name :Marathon
# Problem Link :https://codeforces.com/contest/1692/problem/0
# imput Operation
import sys
test=int(sys.stdin.readline())
for i in range(test):
    arr=list(map(int,sys.stdin.readline().split()))
    trim=arr[0]
    out=0
    for i in range(len(arr)):
        if trim<arr[i]:
            out+=1
    print(out)