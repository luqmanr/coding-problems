# 1. say there is a sorted list L with length N
# 2. we want to search element E in L
# 3. first, pick the middle element of L
# 4. if L[N/2] == E: return E
# 5. if L[N/2] != E:
#       if E > L[N/2]:
#           L = L[(N/2 + 1):N]
#       else:
#           L =  L[0:(N/2 -1)]
# 6. if length(L) == 1:
#       if E == L[0]:
#           return E
#       else:
#           return None (not found)

def bisection_search(L, e):
    def helper(L, e, low, high):
        # if part to search is only length of 1
        if high == low:
            # check if the val equals element we're searching
            return L[low] == e
        
        # get mid point index
        mid = (low + high) // 2
        print(low, high, mid)
        # if mid point equals element we're searching
        if L[mid] == e:
            return True, mid
        elif L[mid] > e:
            if low == mid:      #nothing left to search
                return False, None
            else:
                return helper(L, e, low, mid - 1)
        else:
            return helper(L, e, mid + 1, high)
    
    if len(L) == 0:     #not found
        return False, None
    else:
        return helper(L, e, 0, len(L) - 1)

if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    e = 11
    res = bisection_search(L, e)
    print(res)
    