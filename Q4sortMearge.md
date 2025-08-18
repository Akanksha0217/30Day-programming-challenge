# You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

def mergeArrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    i = j = 0
    result = []

    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < m:
        result.append(arr1[i])
        i += 1
    while j < n:
        result.append(arr2[j])
        j += 1

    return result


arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
merged = mergeArrays(arr1, arr2)
print("Merged Array:", merged)
