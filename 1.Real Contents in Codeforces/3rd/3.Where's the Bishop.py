# Problem Name :Where's the Bishop
# Problem LinK : https://codeforces.com/contest/1692/problem/C
# imput Operation
#ONly Trial Not pass any test case
import sys
test=int(sys.stdin.readline())
for i in range(test):
    arr=[]
    out=[]
    for j in range(8):
        arr.append(sys.stdin.readline().split())
    print(arr)
    for i in range(8):
            out.append(arr[i][0].count("#"))
    for i in range(1.8):
        if out[i]==1 and out[i-1]==2 and out[i+1]==2:
            print(arr[i]+1,arr[i])

