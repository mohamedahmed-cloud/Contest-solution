# Problem Name : 3SUM
# Problem Link : https://codeforces.com/contest/1692/problem/F
# Time Limit in test four
# imput Operation
import sys
test=int(sys.stdin.readline())
for i in range(test):
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    how=0
    # Output Operation
    for i in range(n-2):   
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if i!=j and i!=k and j!=k:
                        num=arr[i]+arr[j]+arr[k]
                        # print(num)
                        str1=str(num)
                        if str1[-1]=="3":
                            print("YES")
                            how=1
                            break
                if how==1:
                    break
            if how==1:
                break
    if how==0:
        print("NO")
        
        
