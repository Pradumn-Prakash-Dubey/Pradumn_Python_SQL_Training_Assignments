
from linked_list2 import LinkedList


def find_primes(self):
        prime_numbers = []
        current = self._first

        while current is not None:
            if self.is_prime(current._value):
                prime_numbers.append(current._value)
            current = current._next

        return prime_numbers

def find_evens(self):
        even_numbers = []
        current = self._first

        while current is not None:
            if current._value % 2 == 0:
                even_numbers.append(current._value)
            current = current._next

        return even_numbers

def is_prime(self, num):
        if num <= 1:
            return False
        else:
             for i in range(2,num):
                  if num % i==0:
                       return False
             return True

def list_sort(self):
    swapped = 0
    lptr = None;
    if (self._first == None):
        return;
      
    while True:
        swapped = 0;
        ptr1 = self._first;  
        while (ptr1._next != lptr):       
            if (ptr1._value > ptr1._next._value):           
                ptr1._value, ptr1._next._value = ptr1._next._value, ptr1._value
                swapped = 1;       
            ptr1 = ptr1._next;       
        lptr = ptr1;    
        if swapped == 0:
            break
def display(self):
        current = self._first
        while current is not None:
            print(current._value, end = ' ')
            current = current._next
            

        

if __name__ == "__main__":
    LinkedList.find_primes = find_primes
    LinkedList.find_evens = find_evens
    LinkedList.is_prime = is_prime
    LinkedList.list_sort = list_sort
    LinkedList.display = display


    linked_list=LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(11)
    linked_list.append(9)

    # print(linked_list.insert(8,10))
    # print(linked_list.remove(9))
    # print(linked_list.get(9))
    # print(linked_list.set(5,4))
    # print(linked_list.size())
    # print(linked_list.info())
    # linked_list.clear()
print( linked_list.find_primes())
print( linked_list.find_evens())
list_sort(linked_list)
linked_list.display()




