


arr = [1, 2, -3, 3, -1, 2]
n = len(arr)

result = []

for i in range(n):
    total = 0
    for j in range(i, n):
        total += arr[j]
        if total == 0:
            result.append((i, j))

print("Subarrays with sum 0:", result)
