/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
*/

package main

import (
	"fmt"
	"math"
)

// One algorithm that can be used to check if a number is prime is to simply
// try dividing it by every integer from 2 to its square root.
// If the remainder upon each division is not zero, the number is prime.

// x - which prime number you'd like
func calculatePrime(x int) int {
	answer := 0

	// Current prime number to return
	primeNumber := 2
	for i := 1; i <= x; i++ {
		// Loop until next prime number found
		for {
			limit := int(math.Sqrt(float64(primeNumber)))
			flag := false
			// Find if number from 2 to limit has remainder or not
			for j := 2; ; j++ {
				if primeNumber%j != 0 || primeNumber == 2 {
					flag = true
					// Break out when higher than limit
					// Not using in for loop because I want to run at least
					// once
					if j > limit {
						break
					} else {
						continue
					}
				} else {
					flag = false
					break
				}

			}
			if flag {
				answer = primeNumber
				primeNumber++
				break
			}
			primeNumber++
		}
	}

	return answer
}

func main() {
	fmt.Println(calculatePrime(10001))
}
