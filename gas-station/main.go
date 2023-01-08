// Steps to solve
/*
1. Check if sum of first_array and second_array is the same, otherwise, there won't be a solution
2. This is probably a BFS problem, so we need to start searching from each level of gas station traversal
2. Wait no. Before that, we need to find all the indices where gas[i] >= cost[i]
3. Because if gas[i] < cost[i], the car can't move from the starting gas station
4. In other words, we need to find the starting point
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

	// find possible starting points
	startingStations := []int{}
	for i, g := range gas {
		if g >= cost[i] {
			startingStations = append(startingStations, i)
		}
	}
	fmt.Printf("possible starting indices: %d\n", startingStations)

	// for each indices, start a bfs
	// NOTE: REFRESH ON BFS -> THIS IS A BASIC ALGORITHM, SHOULD BE ON THE BACK OF MY MIND
	// queue := []int{}

	return 0
}

func main() {
	// testcase1
	gas := []int{1,2,3,4,5}
	cost := []int{3,4,5,1,2}
	res1 := canCompleteCircuit(gas, cost)
	fmt.Printf("testcase1: %d\n", res1)
}