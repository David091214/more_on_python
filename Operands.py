n = int(input())
cnt = 0
while n > 0:
    total = sum(int(c) for c in str(n))
    n -= total
    cnt += 1
print(cnt)
