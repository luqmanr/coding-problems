## MergeSort( )
**Input:** array _A_ of _n_ distinct integers
**Output:** array with the same integers, sorted from smallest to largest.
___________________________________________________________________________
// ignoring base cases
C := recursively sort first half of _A_
D := recursively sort second half of _A_

return Merge(_C, D_)

## Merge( )
**Input:** sorted arrays C and D (length of n/2 each)
**Output:** sorted array B (length n).
**Assumption:** n is even.
____________________________________________________________________________
i := 1
j := 1
for k := 1 to _n_ do
    if C[i] < D[j] then
        B[k] := C[i]
        i += 1
    else
        B[k] := D[j]
        j += 1