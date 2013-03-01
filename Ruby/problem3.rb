#!/usr/bin/env ruby
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Created 2/22/2013


def brute_force_prime(num)
  factors = []
  half = num/2
  counter = 2
  while counter < half
    if num % counter == 0
      factors << counter
      num = num/counter
      #if counter % 100 == 0
        puts "Currently at #{counter}"
      #end
    else 
      counter += 1
    end
  end
  puts factors
end


brute_force_prime(600851475143)
