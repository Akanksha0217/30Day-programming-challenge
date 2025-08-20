#You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.Input:
# An integer array arr of size n where n represents the number of elements in the array.


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
