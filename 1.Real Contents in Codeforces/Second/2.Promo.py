# This Problem I solved it by Time Limit Exceeded.
# Problem Name : Promo
# Problem Link : https://codeforces.com/contest/1697/problem/B
# Input Operation :
# #########################################################################
# Input Operation :
# My Solution 
# Pass all 
import sys
input_From_Sys=sys.stdin.readline
n,q=map(int,input_From_Sys().split())
a=list(map(int,input_From_Sys().split()))
a.sort()
b=[0]
for i in a:
    b.append(b[-1]+i)
    # Output Operation :
for _ in range(q):
    l,r=map(int,input_From_Sys().split())
    print(b[n-l+r]-b[n-l]) 
# #########################################################################
# time limit
import sys
input_From_Sys=sys.stdin.readline
n,q= map(int, input_From_Sys().split())
narr=list(map(int, input_From_Sys().split()))
narr.sort()
for i in range(q):
    x,y=map(int, input_From_Sys().split())
    # Output Operation :
    sell=narr[-x:]
    print(sum(sell[:y]))
  