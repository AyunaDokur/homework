numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
cnt_of_zero = 0
for i in range(2, len(numbers)+1):
    is_prime = True
    for j in range(2,i+1):
        res = i % j
        if res == 0 and i !=j :
            is_prime = False
            break
    if is_prime is True:
        primes.append(i)
    else:
        not_primes.append(i)
print('Простые числа:', primes) #  [2, 3, 5, 7, 11, 13]
print('Не простые числа: ',not_primes) #[4, 6, 8, 9, 10, 12, 14, 15]