def solve():
    n = int(input().strip())
    timeseries = list(map(int, input().split()))
    k = int(input().strip())
    result = []
    for begin_index in range(n - k + 1):
        end_index = begin_index + k
        current_sum = 0
        for v in timeseries[begin_index : end_index]:
            current_sum += v
        current_avg = current_sum / k
        result.append(current_avg)
    print(*result)
if __name__ == "__main__":
    solve()