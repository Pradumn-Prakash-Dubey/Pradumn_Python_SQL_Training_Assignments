import time

def performance_log(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken to execute: {time_taken} seconds")
        return result
    return inner

@performance_log
def find_primes(min, max):
    primes = []
    for num in range(min+1, max):
        for x in range(2,num):
            if num % x==0:
                break
        else:
            primes.append(num)
    return primes

x = find_primes(2, 5000)
print(len(x))