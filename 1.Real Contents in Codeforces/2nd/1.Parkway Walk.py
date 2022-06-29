# Problem Name : Parkway Walk
# Problem Link : https://codeforces.com/contest/1697/problem/A
# Input Operation :
test=int(input())
for i in range(test):
    n,m=map(int,input().split())
    arr=list(map(int, input().split()))
# Output Operation :
    if sum(arr)-m>=0:
        print(sum(arr)-m)
    else:
        print(0)