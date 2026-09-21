def twosum(numbers, X):
    n = len(numbers)  # Исправление: добавляем эту строку
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == X:
                return numbers[i], numbers[j]
    return None

n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

result = twosum(numbers, k)
if result:
    print(result[0], result[1])
else:
    print(None)