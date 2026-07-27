n = int(input())
a = list(map(int, input().split()))
e = a[0]
s = a[0]
for i in range (1, n):
    e = max(a[i], e + a[i])
    s = max(s, e)
print(s)
