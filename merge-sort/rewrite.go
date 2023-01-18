package main

import "log"

func MergeSort(toSortArr []int) []int {
	arrLength := len(toSortArr)
	if arrLength == 2 {
		if toSortArr[0] < toSortArr[1] {
			return toSortArr
		} else {
			return []int{toSortArr[1], toSortArr[0]}
		}
	}
	firstHalf := toSortArr[:arrLength/2]
	secondHalf := toSortArr[arrLength/2:]
	log.Println(firstHalf, secondHalf)
	sortedFirstHalf := MergeSort(firstHalf)
	sortedSecondHalf := MergeSort(secondHalf)
	return Merge(sortedFirstHalf, sortedSecondHalf)
}

func Merge(firstHalf, secondHalf []int) (sortedArr []int) {
	i := 0
	j := 0
	for i < len(firstHalf) && j < len(secondHalf) {
		if firstHalf[i] < secondHalf[j] {
			sortedArr = append(sortedArr, firstHalf[i])
			i++
		} else {
			sortedArr = append(sortedArr, secondHalf[j])
			j++
		}
	}
	for i < len(firstHalf) {
		log.Println("copying rest of first half")
		sortedArr = append(sortedArr, firstHalf[i])
		i++
	}
	for j < len(secondHalf) {
		log.Println("copying rest of second half")
		sortedArr = append(sortedArr, secondHalf[j])
		j++
	}
	return
}


func main() {
	// test case 1
	sortedArr := MergeSort([]int{1,5,7,4,2,8,3,6})
	log.Println(sortedArr)
}