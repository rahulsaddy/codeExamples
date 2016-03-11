
# Multiples of 3 and 5 below 1000
from math import *
def mul35
  numbers = range(1001)
  list_of_35 = [n for n in range(1001) if (n % 3 == 0 or n % 5 == 0) and n != 0]
  prod_of_35 = reduce(lambda a,b: a*b, list_of_35)
  
  
# Fibonacci numbers / even fibonacci numbers
def fib
  numbers = range(11)
  fibo    = [0, 1]
  fibo_even = []
  for i in numbers:
    fibo_i =  fibo[i]+ fibo[i+1]
	fibo.append(fibo_i)
  fibo_even = [n for n in fibo if (n%2 == 0)]
  
    
# what is the index of the Fibonacci number with 1000 digits
len_fibo = 1
idx_fibo = 1 
fibo     = [0, 1]
while len_fibo < 1000:
  fibo_new = fibo[0] + fibo[1]
  fibo[0] = fibo[1]
  fibo[1] = fibo_new
  len_fibo = len(str(fibo_new))
  idx_fibo = idx_fibo + 1 
  
	