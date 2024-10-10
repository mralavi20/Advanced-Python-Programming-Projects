def is_prime (num):
    if (num == 2):
        return 1
    if (num == 1):
        return 0
    for i in range (2, int ((num / 2) + 1)):
        if (num % i == 0):
            return 0
    return 1

def prime_num (num):
    sum_prime = 0
    for i in range (2, int ((num / 2) + 1)):
        if (num % i == 0 and is_prime (i) == 1):
            sum_prime = sum_prime + 1
    if (num != 2 and is_prime (num) == 1):
        sum_prime = sum_prime + 1
    return sum_prime

prime_count = 0
max_num = 0
for i in range (10):
    num = int (input ())
    a = prime_num (num)
    if (a > prime_count):
        prime_count = a
        max_num = num
    if (a == prime_count and num > max_num):
        max_num = num
print (max_num, prime_count)
