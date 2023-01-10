# Implement this!

### KARATSUBA
```
Input: two n-digit positive integers x and y.
Output: the product of x * y.
Assumption: n is a power of 2.
```

Pseudocode:
```
func karatsuba(x, y):
    if n == 1:                                  # base case
        return x * y
    else:                                       # recursive case
        a,b := first and second halves of x
        c,d := first and second halves of y

        p := a + b
        q := c + d

        ac := karatsuba(a, c)
        bd := karatsuba(b, d)
        pq := karatsuba(p, q)

        adbc := pq - ac - bd

        return (10**len(x) * ac) + (10**(len(x)/2) * adbc) + bd
```