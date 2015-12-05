'''
Created on Nov 24, 2010
@author: Charles
A Pythagorean triplet is a set of three natural numbers, 
a  b  c, for which:
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
'''

#Euclid's formula is used to find Pythagorean triplets.
#For 2 arbitrary numbers m and n where m > n:
# a = m^2-n^2 b = 2mn c = m^2 + n^2

m = 2
n = 1

def calc_trip(m, n):
    return (m**2 - n**2, 2*m*n, m**2 + n**2)

#print(calc_trip(m, n))
while(1):
    triplet = calc_trip(m,n)
    if(triplet[0] + triplet[1] + triplet[2] < 1000): 
        print(str(n) + " and " + str(m) + " produce the triplet: " +
              str(triplet) + " where the sum does not add up to 1000")
        m+=1
        continue
    elif (triplet[0] + triplet[1] + triplet[2] == 1000):
        print "M of {} and N of {} makes {}".format(str(m), str(n), triplet)
        print "{} + {} + {} = 1000".format(str(triplet[0]), str(triplet[1]), str(triplet[2]))
        break
    else:
        n+=1
        m = n+1
