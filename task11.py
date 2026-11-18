n = int(input().strip())
arr = list(map(int, input().strip().split()))

swapped = True
was_any_swap = False

while swapped:
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            was_any_swap = True

    if swapped:
        print(' '.join(map(str, arr)))

if not was_any_swap:
    print(' '.join(map(str, arr)))