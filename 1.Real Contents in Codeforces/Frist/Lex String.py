# Problem Name : Lex String
# Problem Link :https://codeforces.com/contest/1689/problem/A
# Input Operation 
test=int(input())
for i in range(test):
    n,m,k=map(int,input().split())
    a=input()
    b=input()
    # Convert a String to Array 
    arra=[]
    arra[:]=a
    arrb=[]
    arrb[:]=b
    arra.sort()
    arrb.sort()
    strout=""
    count1=0
    count2=0
    # Output Operation 
    while arra and arrb:
        if (arra[0]<=arrb[0] and count2<k ) or count1>=k :
            strout+=arra[0]
            arra=arra[1:]
            count2+=1
            count1=0
        elif (arra[0]>arrb[0] and count1<k) or count2>=k:
            strout+=arrb[0]
            arrb=arrb[1:]
            count1+=1
            count2=0
    print(strout)



