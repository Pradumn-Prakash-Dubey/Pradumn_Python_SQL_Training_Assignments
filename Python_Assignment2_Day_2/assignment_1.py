def freq_distribution(lst):
 frequency = {}
 for item in lst:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
 print(frequency)


lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
freq_distribution(lst)
