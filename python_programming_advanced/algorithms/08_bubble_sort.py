numbers = [int(x) for x in input().split()]
is_sorted = False
idx = 0

while not is_sorted:
    is_sorted = True

    for j in range(1, len(numbers) - idx):
        if numbers[j - 1] > numbers[j]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            is_sorted = False

    idx += 1

print(*numbers)
