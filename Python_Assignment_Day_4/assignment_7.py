def freq_dist(lst):
 frequency = {}
 for item in lst:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
 return frequency



def plot_histogram(freq_dist, design = '+++ ', align=False, show_values = True):
    a=0
    align_spacing = 0
    max_value=max(freq_dist.values())
    for key, value in freq_dist.items():
       
     if(align):
        
        a=len(design)
        align_spacing = (a*max_value) +1

 

    for key, value in freq_dist.items():

        bar=f'{key} | {design * value}'
        b=value*a   
        if(show_values):
            bar+=(f'{value}'.rjust(align_spacing-b))
            print(bar)
        else:
           print(bar)
        
lst=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5]
c=freq_dist(lst)
plot_histogram(c, design = '+++ ',align=True, show_values = True)


