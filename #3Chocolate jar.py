#3.Chocolate jar

l = list(map(int, input().split()))
n = int(input())
c = 0
for i in l:
    if i%3 == 0:
        c += i//3
    elif i%3 != 0:
        c += l+i//3
print(c)