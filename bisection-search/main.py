def bisection_search(L, e):
    def helper(L, e, low, high):
        if low == high:
            if L[low] == e:
                return True, low
            else:
                return False, None
        
        mid = (low + high) // 2
        if L[mid] == e:
            return True, mid
        elif L[mid] < e:
            # print(f'using high {low, mid, high}')
            return helper(L, e, mid+1, high)
        else:
            # print(f'using low {low, mid, high}')
            return helper(L, e, low, mid-1)

    return helper(L, e, 0, len(L)-1)

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