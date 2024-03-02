def is_Prime(num):
    if num <= 2:
        return True
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

def prime_In_Range(start, end):
    return [num for num in range(start, end+1) if is_Prime(num)]

print(prime_In_Range(3,50))