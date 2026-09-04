k = int(input())
field = []
for _ in range(4):
    field.append(input().strip())
all_symbols = ''.join(field)
point = 0
for t in range(1, 10):
    count = all_symbols.count(str(t))
    if count > 0 and count <= 2 * k:
        point += 1
print(point)