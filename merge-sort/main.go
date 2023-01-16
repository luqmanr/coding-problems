package main

import "fmt"

func Merge(C, D []int) (B []int) {
	i := 0
	j := 0

	// traverse C and D array
	// if we reach one of the end of the arrays
	// break the loop, then continue to the next loop
	for i < len(C) && j < len(D) {
		if C[i] < D[j] {
			B = append(B, C[i])
			i += 1
		} else {
			B = append(B, D[j])
			j += 1
		}
	}

	// if there are any elements left in C array
	// copy it to B array
	for i < len(C) {
		B = append(B, C[i])
		i += 1
	}
	// if there are any elements left in D array
	// copy it to B array
	for j < len(D) {
		B = append(B, D[j])
		j += 1
	}

	return
}

func MergeSort(A []int) []int {
	if len(A) == 2 {
		if A[0] < A[1] {
			return A
		} else {
			return []int{A[1], A[0]}
		}
	}

	C := A[:len(A)/2]
	D := A[len(A)/2:]
	fmt.Println("before:", C, D)

	CSorted := MergeSort(C)
	DSorted := MergeSort(D)
	B := Merge(CSorted, DSorted)
	fmt.Println("sorted:", B)
	return B
}

func main() {
	Final := MergeSort([]int{5,4,1,8,7,2,6,3})
	fmt.Println("final:", Final)
}