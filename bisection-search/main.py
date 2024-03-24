def bisection_search(L, e):
    def helper(L, e, low, high):
        # find mid point
        mid = (low + high) // 2
        if mid == low:
            if e == L[mid]:
                return True, mid

        if L[mid] == e:
            return True, mid
        elif e > L[mid]:
            if mid == high:     # nothing left to search
                return False, None
            return helper(L, e, mid + 1, high)
        else:
            if low == mid:
                return False, None
            return helper(L, e, low, mid - 1)
    
    return helper(L, e, 0, len(L) - 1)

if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    e = 11
    res = bisection_search(L, e)
    print(f'case 1 : {res}')
    
    e = 3
    res = bisection_search(L, e)
    print(f'case 2 : {res}')

    e = 7
    res = bisection_search(L, e)
    print(f'case 3 : {res}')
    
    e = 0
    res = bisection_search(L, e)
    print(f'case 4 : {res}')
    
    e = -5
    res = bisection_search(L, e)
    print(f'case 5 : {res}')