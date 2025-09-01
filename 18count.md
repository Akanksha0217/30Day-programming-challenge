import math
def count_divisors(N: int) -> int:
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i * i == N:
                count += 1   # perfect square → count only once
            else:
                count += 2   # count both i and N//i
    return count
print(count_divisors(12))  
print(count_divisors(18))   
print(count_divisors(29))   
print(count_divisors(100))  
print(count_divisors(1))
print(count_divisors(997))  
print(count_divisors(36))   
