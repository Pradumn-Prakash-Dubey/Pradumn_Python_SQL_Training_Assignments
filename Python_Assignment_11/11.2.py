import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, t, e, s):
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return self.time_taken


    def find_primes(self,min, max):
        primes = []
        for num in range(min+1, max):
            for x in range(2,num):
                if num % x==0:
                    break
            else:
                primes.append(num)
        return primes

with Timer() as t:
    t.__enter__()
    p = t.find_primes(2, 11000)
    print('Total Prime Numbers', len(p))
    t.__exit__(None,None,None)
    print('Total time taken', t.time_taken)
   