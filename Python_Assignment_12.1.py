import time

def cached(func):
    cache={}
    def wrapper(*args):
        for argv in args:
         results = cache.get(argv)
        if not results:
            
            results = func(*args)
            cache.setdefault(argv, results)
            return results
        else:
            print(cache[argv])
            return results
    return wrapper

def performance_monitor(func):
    def inner(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken to execute: {time_taken} seconds")
        return result
    return inner

@cached
@performance_monitor
def factorial(n):
    fn=1
    for i in range(1,n+1):
        time.sleep(0.5)
        fn*=i
    return fn

r1=factorial(5)
r2=factorial(7)
r3=factorial(5)





