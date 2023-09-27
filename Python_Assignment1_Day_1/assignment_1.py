count=int(input('count'))
max=None
for i in range(count):
    num=int(input('num'))
    if max==None or num>max :
        max=num
    else:
        pass
    
print(max)