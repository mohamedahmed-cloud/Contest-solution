arr=[4 ,3 ,2, 5]
arr.sort()
out=0
for i in range(1,len(arr)-1):
    if i==len(arr)//2:
        continue
    out+=arr[i]^arr[i-1]
    print(out)