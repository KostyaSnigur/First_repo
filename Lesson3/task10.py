def factorial(n):
    if n <= 1:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)
factorial(1)  

n = 50
k = 7

def number_of_groups(n, k):
    if n < k:
        return 0
    return  factorial(n) / (factorial(n - k) * factorial(k))
Cnk = number_of_groups(n, k)
print(Cnk)
Cnk = n! / ((n - k)! · k!)