def is_prime(func):
    def wrapper(a,b,c):
        n = func(a,b,c)
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        print(n)
        if d*d > n:
            return 'Простое'
        else:
            return 'Составное'
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)