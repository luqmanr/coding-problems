// Steps to solve
/*
1. Check if sum of first_array and second_array is the same, otherwise, there won't be a solution
2. This is probably a BFS problem, so we need to start searching from each level of gas station traversal

*/
package main

import "fmt"

func sum(intSlice []int) int {
	sum := 0
	for _, e := range intSlice {
		sum += e
	}
	return sum
}

func canCompleteCircuit(gas []int, cost []int) int {
    gasSum := sum(gas)
	costSum := sum(cost)
	fmt.Printf("gas sum: %d\n", gasSum)
	fmt.Printf("cost sum: %d\n", costSum)

	// if gas sum != cost sum, it's impossible to complete the circuit
	if gasSum != costSum {
		return -1
	} 

	return 0
}

func main() {
	// testcase1
	gas := []int{1,2,3,4,5}
	cost := []int{3,4,5,1,2}
	res1 := canCompleteCircuit(gas, cost)
	fmt.Printf("testcase1: %d\n", res1)
}