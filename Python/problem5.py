#2520 is the smallest number that can be divided 
#by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is 
#evenly divisible by all of the numbers from 1 to 20?

#incrementing by 1
#First run: 203.5535704
#Second run: 101.09164728

#increment by 20
#First run: 14.59304404
#Second run: 7.81668156

import time

start_time = time.clock()
x = 20
while(1):
    retval = 0
    if(x % 1 == 0 and x % 2 == 0 and x % 3 == 0 and x % 4 == 0
       and x % 5 == 0 and x % 6 == 0 and x % 7 == 0 and x % 8 == 0
       and x % 9 == 0 and x % 10 == 0 and x % 11 == 0 and x % 12 == 0
       and x % 13 == 0 and x % 14 == 0 and x % 15 == 0 and x % 16 == 0
       and x % 17 == 0 and x % 18 == 0 and x % 19 == 0 and x % 20 == 0):
        print(x)
        break
    else:
        x += 20
stop_time = time.clock()

print("First run: " + str(stop_time - start_time))

start_time = time.clock()
x = 20
while(1):
    if(x % 20 == 0 and x % 19 == 0 and x % 18 == 0 and x % 17 == 0
       and x % 16 == 0 and x % 15 == 0 and x % 14 == 0 and x % 13 == 0
       and x % 12 == 0 and x % 11 == 0 and x % 10 == 0 and x % 9 == 0
       and x % 8 == 0 and x % 7 == 0 and x % 6 == 0 and x % 5 == 0
       and x % 4 == 0 and x % 3 == 0 and x % 2 == 0 and x % 1 == 0):
        print(x)
        break
    else:
        x += 20
stop_time = time.clock()

print("Second run: " + str(stop_time - start_time))