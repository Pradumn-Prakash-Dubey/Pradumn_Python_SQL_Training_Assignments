total=int(input("total values?"))

count=1
max=int(input("number#1?"))
max2=None 

while count<total:
    count+=1
    value=int(input(f"number#{count}? "))
    if value>max:
        max2=max
        max=value
    elif value<max and (max2==None or value>max2) :
        max2=value

if max!=max2:
    print(f'second highest is {max2}')
else:
    print(f'All values are same. No second hightest')