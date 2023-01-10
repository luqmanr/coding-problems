package main

import (
	"fmt"
	"math"
)

func getDecimalDigits(num int) uint {
	var result uint

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

func getHighAndLowDigits(num int, digits uint) (int, int) {
	divisor := int(math.Pow(10, float64(digits)))
	if num >= divisor {
		fmt.Println(num / divisor, num % divisor)
		return num / divisor, num % divisor
	} else {
		fmt.Println(0, num)
		return 0, num
	}
}

func Karatsuba(x int, y int) int {
	var max_digits uint

	if x == 0 || y == 0 {
		return 0
	}

	if x < 10 || y < 10 {
		return x * y
	}

	x_digits := getDecimalDigits(x)
	y_digits := getDecimalDigits(y)

	if x_digits >= y_digits {
		max_digits = x_digits / 2
	} else {
		max_digits = y_digits / 2
	}

	x_high, x_low := getHighAndLowDigits(x, max_digits)
	y_high, y_low := getHighAndLowDigits(y, max_digits)

	z0 := Karatsuba(x_low, y_low)
	z1 := Karatsuba((x_low + x_high), (y_low + y_high))
	z2 := Karatsuba(x_high, y_high)

	return (z2 * int(math.Pow(10, float64(2*max_digits)))) + (z1-z2-z0)*int(math.Pow(10, float64(max_digits))) + z0
}

func main() {
	// testcase 1
	x := 5678
	y := 1234
	res1 := Karatsuba(x, y)
	fmt.Printf("tetcase 1 res: %d vs %d\n", res1, x*y)
}