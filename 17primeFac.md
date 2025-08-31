def prime_factorization(N: int) -> list:
    factors = []
    i = 2
    while N > 1:
        if N % i == 0:
            factors.append(i)
            N //= i
        else:
            i += 1
    return factors


print(prime_factorization(18))     
print(prime_factorization(30))      
print(prime_factorization(49))       
print(prime_factorization(19))      
print(prime_factorization(64))      
print(prime_factorization(123456))   

