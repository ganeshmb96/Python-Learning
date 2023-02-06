#trying out python lambda functions
output = (lambda x: x+1)

ans = output(3)
print(ans)

#Printing the full name of a person using lambda strings
full_name = lambda first, last : f'Full name:{first.title()} {last.title()}'
print(full_name('ganesh', 'bhat'))

#Using a lambda function with recursion
high_ord_func = lambda x,func : x+func(x)
print(high_ord_func(2, lambda x:x*x))