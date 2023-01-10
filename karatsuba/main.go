package main

import (
	"fmt"
	"math"
	"strconv"
)

func CountDigit(n int) int {
	// if input digit is 0, should we count it as 1 digit?
	if n == 0 {
		return 1
	}
	// else, divide int by 10, removing the least significant digit
	// while counting how many loops are done -> this count
	// is how many digits is the number
	count := 0
   	for n > 0 {
		n = n/10
    	count++
   	}
	return count
}

func Karatsuba(x, y int) int {
	fmt.Printf("x: %d, y: %d\n", x,y)
	xStr := strconv.Itoa(x)
	yStr := strconv.Itoa(y)

	if len(xStr) <= 1 || len(yStr) <= 1 || x == 0 || y == 0 {
		fmt.Printf("multiplying %d * %d = %d\n", x, y, x*y)
		return x * y
	}

	a, _ := strconv.Atoi(xStr[:len(xStr)/2])
	b, _ := strconv.Atoi(xStr[len(xStr)/2:])
	c, _ := strconv.Atoi(yStr[:len(yStr)/2])
	d, _ := strconv.Atoi(yStr[len(yStr)/2:])

	fmt.Printf("X: first half: %d, second half: %d\n", a, b)
	fmt.Printf("Y: first half: %d, second half: %d\n", c, d)

	p := a + b
	q := c + d	

	ac := Karatsuba(a, b)
	bd := Karatsuba(c, d)
	pq := Karatsuba(p, q)

	adbc := pq - ac - bd

	k := int(math.Pow(10, float64(len(xStr)))) * ac
	l := int(math.Pow(10, float64(len(xStr)/2))) * adbc

	fmt.Printf("end of recursion, result: %d\n", k + l + bd)
	return k + l + bd
}

func main() {
	// testcase 1
	x := 5678
	y := 1234
	res1 := Karatsuba(x, y)
	fmt.Printf("tetcase 1 res: %d vs %d\n", res1, x*y)
}