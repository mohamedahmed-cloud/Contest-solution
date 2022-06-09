# Input Operation 
import math


test=int(input())

# Output Operation
for i in range(test):
    num=int(input())
    h1,h2,h3=0,0,0
    while(num!=h1+h2+h3):
        h1+=1
        if(h1>h2 and (h1+h2+h3+1)<num):
            h2+=1
        if(h2>h3+1 and (h1+h2+h3+1)<num):
                h3+=1
    print(h2,h1,h3)
