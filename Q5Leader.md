#You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.

arr = [16, 17, 4, 3, 5, 2]
Leaders=[]
n=len(arr)

for i in range(n):
      if all(arr[i]>arr[j] for j in range(i+1,n)):
         Leaders.append(arr[i])

print("Leaders :",Leaders)
