/*
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	stringConversion := strconv.Itoa(x)
	r := []rune(stringConversion)
	mid := len(r) / 2
	end := len(r) - 1
	for i := 0; i < mid; i++ {
		if r[i] != r[end-i] {
			return false
		}
	}
	return true
}

func main() {
	answer, x, y := 0, 100, 100
	for x < 1000 {
		if isPalindrome(x * y) {
			if (x * y) > answer {
				answer = x * y
				fmt.Println("Current answer is", x, "*", y, "which equals", x*y)
			}
		}
		if y < 1000 {
			y++
		} else {
			y = 100
			x++
		}

	}
	fmt.Println(answer)
}
