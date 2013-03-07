#!/usr/bin/env ruby
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# 
# Created 3/07/2013

highest = 0
100.upto(999) do |x|
  100.upto(999) do |y|
    highest = x * y if x * y > highest and (x*y).to_s == (x*y).to_s.reverse
  end
end

puts highest

