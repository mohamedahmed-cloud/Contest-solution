# Problem Name : Mystic Permutation
# Problem Link : https://codeforces.com/contest/1689/problem/B
# Input Operation 
test=int(input())
for i in range(test):
    n=int(input())
    a=list(map(int, input().split()))
    b=sorted(a)
    # print(a)
    # Output Operation
    if n==1:
        print(-1)
    else:
        for i in range(n-1):
            if a[i]==b[i]:
                b[i],b[i+1]=b[i+1],b[i]
        if a[-1]==b[-1]:
            b[-1],b[-2]=b[-2],b[-1]
        print(*b)
        
