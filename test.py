import random
list_res = []
def rand_first_number():
    n = random.randint(3, 10)
    return n
def password_result(n):
    for i in range(0, n):
        for j in range(1,i):
            #print(i)
            #sum_of_pair = j+i
            res = n%(j+i)
            if res == 0:
                list_res.append(i)
                list_res.append(j)
            #print(i, j, sum_of_pair, res)
    #list_res.reverse()
    print(list_res)
        #list_res.clear()



first_number = rand_first_number()
print(first_number)
password_result(first_number)
