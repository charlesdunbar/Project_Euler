#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 
#2-digit numbers is 9009 = 91  99.

#Find the largest palindrome made from the 
#product of two 3-digit numbers.

def isPalindrome(num):
    strnum = str(num)
    return strnum == strnum[::-1] #Slice the whole line, step by -1

y = 999
largest = 0
bigx = 0
bigy = 0
for y in range(999, 0, -1):
    for x in range(999, 0, -1):
        if(isPalindrome(x*y)):
            if( (x*y) > largest): largest = x*y; bigx = x; bigy = x
            #print(x, y); print(x*y)
            break
        #else: 
            #print(str(x) + " times " + str(y) +" is " + str(x*y))
    print(str(largest) + " is the largest, being the product of " + str(bigx) +" and " + str(bigy))
        
