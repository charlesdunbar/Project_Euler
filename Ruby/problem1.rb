#!/usr/bin/env ruby
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
for number in 0..999
  if number % 3 == 0 or number % 5 == 0
    total += number
  end
end
puts "Summation of all numbers that are multiples of 3 and 5 up to 1000 is #{total}"
