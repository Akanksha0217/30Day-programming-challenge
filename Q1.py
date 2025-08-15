# You are given an array arr consisting only of 0s, 1s, and 2s. The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space. This means you need to rearrange the array in-place.

# Input:
# An integer array arr of size n where each element is either 0, 1, or 2.
# Example : arr = [0, 1, 2, 1, 0, 2, 1, 0]

# Output:
# The sorted array, arranged in increasing order of 0s, 1s, and 2s.
# Example: [0, 0, 0, 1, 1, 1, 2, 2]
# solution:

def dutch_alg(arr):
    start=0
    current=0
    high=len(arr)-1

    while current <= high:
        if arr[current]==0:
            arr[start],arr[current] =arr[current],arr[start]
            start +=1
            current +=1
        elif arr[current] ==1:
            current += 1
        else:
            arr[current],arr[high]=arr[high],arr[current]
            high -=1
    return arr

numbers=[0, 1, 2, 1, 0, 2, 1, 0]
sorted_arr=dutch_alg(numbers)

print(sorted_arr)
