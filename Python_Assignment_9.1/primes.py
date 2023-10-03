def find_primes(list):
    for list_items in list:
        for n in range(2,int(list_items)):
            if ((int(list_items) % n) == 0):
                print(f"{list_items} is not a prime number")
                break
        else:
            print(f"{list_items} is a prime number")


if __name__ == "__main__":
    list=[]
    number=int(input("Enter number of elements in the list :"))
    for i in range(number):
        num=input("Enter the elements :")
        list.append(num)
    find_primes(list)
    
