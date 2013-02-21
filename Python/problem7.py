'''
Created on Nov 23, 2010

@author: Charles

Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime numbem?

Prime 10001 Found: 104743
'''

#Known: Except for 2 and 5, all prime numbers end in 1 ,3 ,7 or 9
#Wikipedia shows Sieve of Eratosthenes may be a good implementation 
#to start with

#Problem, it's good for finding primes up to a certain digit, not
#for finding x number of prime numbers

#Poor man's solution: iterate through each number, have a counter

prime_list = [2,3,5,7,11,13]
counter = 7
limit = 10001
curCheck = 14


while(counter <= limit):
    strnum = int(str(curCheck)[-1])
    if(strnum == 9 or strnum == 7  or strnum == 3 or strnum == 1): #Except for 2 and 5, all prime numbers end in 1 ,3 ,7 or 9
        for x in range(curCheck-1, 1, -1): #Start at current number - 1 (already know x % x == 0) and stop when you get to 1, decrement each time by 1 to check it's prime        
            if(curCheck % x != 0): continue
            else: curCheck +=1;break
        else: 
            if(curCheck in prime_list):
                continue
            else:
                prime_list.append(curCheck); counter += 1; print("Prime " + str(len(prime_list)) + " Found: " + str(curCheck)); curCheck +=1
    else: #If it the current check ends in a not prime number
        curCheck += 1; continue
            
print(prime_list)
    

        