#Each new term in the Fibonacci sequence is generated 
#by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#Find the sum of all the even-valued terms in the sequence which do not exceed four million.

def fib(i):
    #base case
    if(i == 0): return 0
    x1 = 1; x2 = 1;
    for x in range(3, i+1):
        x3 = x1 + x2
        x1 = x2
        x2 = x3
    return x2
    

def sumfib(i):
    retval = 0
    for x in range(1,i+1): #Starting at 0 for fib() doesn't help
        retval += fib(x)
    return retval

def sumevenfib(i):
    retval = 0
    for x in range(0,i+1,3):#Each multiple of 3 fib number is even 
        retval += fib(x)
  #      print("Retval is currently: " +str(retval))
    return retval

#print(fib(34))
#print(sumfib(20))
#print (sumevenfib(6))
print (sumevenfib(33))
    
