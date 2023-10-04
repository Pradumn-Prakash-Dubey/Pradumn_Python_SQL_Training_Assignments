from math import sqrt

def is_prime(num):        
        if(num<=1 ): 
            return False 
        for x in range(2,int(sqrt(num))+1): 
            if(num%x==0): 
                return False 
        return True

class prime_range:
    def __init__(self, min, max=None):
        
        if max==None:
          self.start=0
          self.end=min
        else:
         self.start=min-1
         self.end=max

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.start += 1
            if self.start > self.end:
                raise StopIteration
            if is_prime(self.start):
                return self.start

for p in prime_range(10):
    print(p,end=' ')
print()

primes=prime_range(5, 91)
it = iter(primes)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


