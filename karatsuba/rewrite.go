package main

import (
	"log"
	"math"
)

func CountDigits(num int) int {
	if num < 10 || num == 0 {
		return 1
	}
	count := 0
	for num > 10 {
		num = num / 10
		count += 1
	}
	return count+1
}

func SplitNum(num int, numDigits int) (high, low int) {
	if num < 10 {
		return 0, num
	}
	divisor := int(math.Pow(10, float64(numDigits/2)))
	high = num / divisor
	low = num % divisor
	return high, low
}

func Karatsuba(x, y int) int {
	if x < 10 || y < 10 || x == 0 || y == 0 {
		return x*y
	}

	digitNumX := CountDigits(x)
	digitNumY := CountDigits(y)
	digitNum := 0

	if digitNumX >= digitNumY {
		digitNum = digitNumX / 2
	} else {
		digitNum = digitNumY / 2
	}

	a, b := SplitNum(x, digitNum*2)
	c, d := SplitNum(y, digitNum*2)

	log.Println(a, b, c, d, (a+b), (c+d))
	
	bd := Karatsuba(b, d)
	pq := Karatsuba((b+a), (d+c))
	ac := Karatsuba(a, c)

	log.Println("bd, pq, ac:", bd, pq, ac)

	p1 := (ac * int(math.Pow(10, float64(digitNum*2))))
	p2 := (pq-ac-bd)*int(math.Pow(10, float64(digitNum)))
	log.Println("p1, p2, bd:", p1, p2, bd)

	return p1 + p2 + bd
}

func main() {
	// // base case
	// x := 9
	// y := 4
	// res0 := Karatsuba(x, y)
	// log.Printf("res0: %d vs %d\n", res0, (x*y))

	// test case 1
	x := 5678
	y := 1234
	log.Printf("testcase1, x: %d, y: %d\n", x, y)
	res1 := Karatsuba(x, y)
	log.Printf("res1: %d vs %d\n", res1, (x*y))
}