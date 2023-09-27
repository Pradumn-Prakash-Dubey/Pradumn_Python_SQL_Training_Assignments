def sum( *arguments):
   result=0
   for value in arguments:
      result+=value
   return result

      

def average(*parameters):
   return sum(*parameters)/len(parameters)
   

ans=average(1,2,3,4)
print(ans)
