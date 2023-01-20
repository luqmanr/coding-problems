package main

import "fmt"

func MergeSort(toSort []int) (sorted []int) {
	arrLen := len(toSort)
	if arrLen <= 2 {
		if toSort[0] < toSort[1] {
			sorted = toSort
			print(sorted)
			return
		} else {
			sorted = []int{toSort[1], toSort[0]}
			print(sorted)
			return
		}
	}
	firstHalf := toSort[:arrLen/2]
	secondHalf := toSort[arrLen/2:]
	fmt.Println(toSort, firstHalf, secondHalf)
	sortedFirstHalf := MergeSort(firstHalf)
	sortedSecondHalf := MergeSort(secondHalf)
	sorted = Merge(sortedFirstHalf, sortedSecondHalf)
	return
}

func Merge(first, second []int) (sorted []int) {
	i := 0
	j := 0
	for i < len(first) && j < len(second) {
		if first[i] < second[j] {
			sorted = append(sorted, first[i])
			print(sorted)
			i += 1
		} else {
			sorted = append(sorted, second[j])
			print(sorted)
			j += 1
		}
 	}

	for i < len(first) {
		sorted = append(sorted, first[i])
		i += 1
	}

	for j < len(second) {
		sorted = append(sorted, second[j])
		j += 1
	}
	return
}

func main() {
	// testcase 1
	res1 := MergeSort([]int{1,6,4,9,3,2,8,7,5})
	fmt.Println(res1)
}