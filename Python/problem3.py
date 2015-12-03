#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

prime_list = [2,3,5,7,11,13,17]

#Prime tests given by Dr.Math
def prime_test(x):
    factors = []
    #Even number
    if(x % 2 == 0):
        factors.append(x/2)
        factors.append(2)
     