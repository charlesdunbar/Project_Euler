/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
*/

package main

import "fmt"

func primeFactor(x int) []int {
	answer := make([]int, 0)
	for i := 2; i <= x; i++ {
		if x%i == 0 {
			answer = append(answer, i)
			x /= i
		}
	}
	return answer
}

func main() {
	// Print last element without needing to calculate primeFactor twice
	// with the len function
	answer := primeFactor(600851475143)
	fmt.Println(answer[len(answer)-1])
}
