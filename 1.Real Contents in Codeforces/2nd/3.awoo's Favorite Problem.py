# Problem Name : awoo's Favorite Problem
# Problem Link : https://codeforces.com/contest/1697/problem/C
# Input Operation :

# This is not the solution this is my trial to solve it 
test=int(input())
for i in range(test):
    n=int(input())
    s1=input()
    s2=input()
# Ouput Operation :
    out=0 
    if s1==s2:
        print("YES")
    elif (s1=="a" and s2=="b") or (s1=="b" and s2=="c"):
        print("YES")
    else:
        for i in range(0,n-2):
            if (s1[i:i+2]=="ab" and s2[i:i+2]=="ba") or (s1[i:i+2]=="bc" and s2[i:i+2]=="cb") or s1[i]==s2[i]:
                out=1
            else :
                print("NO")
                break
        if out==1:
            print("YES")
