def histogram(dict):
 for item in dict:
    a=dict[item]
    print(item,'|','='*a,a)

def freq_dist(lst):
 frequency = {}
 for item in lst:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
 return frequency




lst = []
dict_freq={}
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
dict_freq=freq_dist(lst)
histogram(dict_freq)




