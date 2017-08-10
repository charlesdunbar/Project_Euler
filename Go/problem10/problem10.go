/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

package main

import (
	"fmt"
	"math"
)

// Implement Sieve of Eratosthenes from 2 to x
func sieve(x int) []int {
	var answer []int
	// Fill answer slice
	for i := 2; i <= x; i++ {
		answer = append(answer, i)
	}
	// Only need to run to the sqrt of x iterations
	limit := int(math.Sqrt(float64(x)))
	for i := 0; i < limit; i++ {
		currentNumber := answer[i]
		arrayLocation := i
		// Find next non-zero element in answer
		for {
			if currentNumber == 0 {
				arrayLocation++
				currentNumber = answer[arrayLocation]
			} else {
				break
			}
		}
		// Turn every multiple of currentNumber into 0
		// since it's clearly not prime
		for j := i + 1; j < len(answer); j++ {
			// Don't divide by zero and skip over self checks
			if answer[j] == 0 || answer[j] == currentNumber {
				continue
			}
			if answer[j]%currentNumber == 0 {
				answer[j] = 0
			}
		}
	}
	return answer
}

func main() {
	answer := 0
	for _, v := range sieve(2000000) {
		answer += v
	}
	fmt.Println(answer)
}
