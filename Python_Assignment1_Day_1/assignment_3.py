lower = int(input("Lower boundry: "))
upper = int(input("Upper boundry: "))
for n in range(lower, upper + 1):
    if n==0 or n==1:
        print("Not Prime")
    elif (n > 1):
        for x in range(2, n):
            if ((n % x) == 0):
                print(n, "not prime")
                break
        else:
            print(n, "prime")