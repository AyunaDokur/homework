class ZeroValueError(ValueError):
    pass

def is_prime(func):
    def wrapper(a,b,c):
        n = func(a,b,c)
        print(n)
        if n <= 1:
            raise ZeroValueError()
        if n == 2:
            return 'Простое'
        for i in range(2, n // 2):
            if n % i == 0:
                return 'Составное'
            return 'Простое'
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c

try:
    result = sum_three(0, 0, 0)
    print(result)
except ZeroValueError:
    print('Число не является ни простым, ни составным')