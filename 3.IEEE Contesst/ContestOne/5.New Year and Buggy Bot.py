# Now is 2022-5-10 I can't complete the logic of this problem
# but Hoping taking massive practicing in the problem like this soon. 

# Link on Codeforce
# " https://codeforces.com/problemset/problem/908/B "
# ####################

# input Opertion
x, y = map(int, input().split())
arr = []
for i in range(x+1):
    arr.extend(list(map(str, input().split())))
# output Opertion
Xs = 0
Ys = 0
Xe = 0
Ye = 0
for i in range(x):
    for j in range(y):
        if arr[i][j] == "S":
            Xs = i+1
            Ys = j+1
        if arr[i][j] == "E":
            Xe = i+1
            Ye = j+1
if Xs-Xe<0:
    print("D")
if Ys-Ye<0:
    print("left")
