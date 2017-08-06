/*
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
*/

package main

import "fmt"

func smallestMultiple(x int) int {
	answer := 2 // Start at 2, everything is divisible by 1
	for i := x; i > 1; i-- {
		if answer%i == 0 {
			continue
		} else {
			i = x
			answer++
		}
	}
	return answer
}

func main() {
	fmt.Println(smallestMultiple(20))
}
