n=int(input())
number_house=list(map(int, input().split()))

ans = [0]*n
last_zero = -10**9

for i in range(n):
    if number_house[i]==0:
        last_zero = i
    ans[i] = i - last_zero
next_zero = 10**9
for i in range(n - 1, -1, -1):
    if number_house[i]==0:
        next_zero = i
    dist = next_zero - i

    if dist < ans[i]:
        ans[i] = dist
print(*ans)