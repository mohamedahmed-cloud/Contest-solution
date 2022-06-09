# Link on Codeforce
# " https://codeforces.com/problemset/problem/58/A "
# ####################

# prepration for my code
my_list = list("hello")
count = 0
# input operation
string = input()
# ouput operation
for i in string:
    if count == len(my_list):
        break
    if i == my_list[count]:
        count += 1
if count == len(my_list):
    print("YES")
else:
    print("NO")

