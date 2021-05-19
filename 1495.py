n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp1 = [0 for _ in range(m+1)]
dp2 = [0 for _ in range(m+1)]

dp1[s] = 1
for vol in v:
    for i in range(m+1):
        if dp1[i] != 0:
            if i+vol <= m:
                dp2[i+vol] = 1
            if i-vol >= 0:
                dp2[i-vol] = 1
    dp1 = dp2
    dp2 = [0] * (m+1)

ans = -1
for i in range(m, -1, -1):
    if dp1[i] != 0:
        ans = i
        break
print(ans)

