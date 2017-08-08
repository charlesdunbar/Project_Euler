/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*/

package main

import (
	"fmt"
)

func isTriplet(a, b, c int) bool {
	if a*a+b*b == c*c {
		return true
	}
	return false
}
func main() {
	for b := 2; b <= 1000; b++ {
		for a := 1; a <= 1000; a++ {
			if isTriplet(a, b, 1000-(a+b)) {
				fmt.Println(a, "*", b, "*", 1000-(a+b),
					"equals", a*b*(1000-(a+b)))
			}
		}
	}
}
