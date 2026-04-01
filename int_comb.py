n = int(input())
m = int(input())
res = 0
current = 0
for _ in range(m):
    current = current * 10 + n
    res += current
print(res)