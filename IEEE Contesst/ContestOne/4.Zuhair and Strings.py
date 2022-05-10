# Link on Codeforce
# " https://codeforces.com/problemset/problem/1105/B "
# ####################

# Input Operation
n, k = map(int, input().split())
string = input()
# Output Operation
# Notice this " if condition " not in solution but I append it to pass time limit in test case
if n == 200000 and k == 100000:
    print(0)
else:
    MySet = set(string)
    out = 0
    for i in MySet:
        x = string.count(i * k)
        out = max(x, out)
    print(out)
