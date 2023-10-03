def find_evens(list):
    for list_items in list:
        if int(list_items) % 2 ==0:
            print(f"{list_items} is an even number")
        else:
             print(f"{list_items} is not an even number")





if __name__ == "__main__":
    list=[]
    number=int(input("Enter number of elements in the list :"))
    for i in range(number):
        num=input("Enter the elements :")
        list.append(num)
    find_evens(list)
    