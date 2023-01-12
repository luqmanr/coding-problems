package main

import (
	"fmt"
	"math"
)

func GetDecimalDigits(num int) uint {
	result := uint(0)
	if num == 0 {
		return 1
	}
	if num < 0 {
		num = -num
	}
	for num > 0 {
		result++
		num = num / 10
	}

	return result
}

// to get high (first half) and low (second half) of a number
// we first divide number by 10^(numDigits/2)
// so ```a,b := n / 10^(nDigits/2)````
// we return the divison as the high, and the remainder as the low
func GetHighAndLowDigits(num int, digits uint) (int, int) {
	divisor := int(math.Pow(10, float64(digits)))
	if num >= divisor {
		fmt.Println(num, divisor, digits, num / divisor, num % divisor)
		return num / divisor, num % divisor
	} else {
		fmt.Println(0, num)
		return 0, num
	}
}

func Karatsuba(x int, y int) int {
	maxDigits := uint(0)
	if x < 10 || y < 10 {
		return x * y
	}

	x_digits := GetDecimalDigits(x)
	y_digits := GetDecimalDigits(y)

	if x_digits >= y_digits {
		maxDigits = x_digits / 2
	} else {
		maxDigits = y_digits / 2
	}

	x_high, x_low := GetHighAndLowDigits(x, maxDigits)
	y_high, y_low := GetHighAndLowDigits(y, maxDigits)

	z0 := Karatsuba(x_low, y_low)
	z1 := Karatsuba((x_low + x_high), (y_low + y_high))
	z2 := Karatsuba(x_high, y_high)

	return (z2 * int(math.Pow(10, float64(2*maxDigits)))) + (z1-z2-z0)*int(math.Pow(10, float64(maxDigits))) + z0
}

func main() {
	// testcase 1
	x := 5678
	y := 1234
	res1 := Karatsuba(x, y)
	fmt.Printf("tetcase 1 res: %d vs %d\n", res1, x*y)
}