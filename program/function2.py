#Return Values
def my_function(x):
  return 5 * x

print(my_function(2))



print("----------------------")

# Positional-Only Arguments
def positiona(x, /):
 print(x)
positiona(3)



#Keyword-Only Arguments
def keyword_only(*,x):
    print(x)
    keyword_only(x=1)













