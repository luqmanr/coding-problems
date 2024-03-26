def merge_sort(L):
    def merge(low, high):
        sorted_list = []
        l = 0
        h = 0

        # iterate over both list, and compare if the one compared is smaller or bigger
        while l < len(low) and h < len(high):
            if low[l] < high[h]:
                sorted_list.append(low[l])
                l += 1
            else:
                sorted_list.append(high[h])
                h += 1
        
        # assume both low and high are sorted list
        # so if we've iterated over one of the list,
        # we just need to copy the rest of the items in the list, to the new list
        while l < len(low):
            sorted_list.append(low[l])
            l += 1
        
        while h < len(high):
            sorted_list.append(high[h])
            h += 1
        
        return sorted_list
    
    # if only 1 element is in the list,
    # the by definition, the list is sorted
    if len(L) == 1:
        return L

    # recursively call merge_sort() function on both low & high
    # until the condition where len(L) == 1
    mid_idx = len(L) // 2
    low = merge_sort(L[:mid_idx])
    high = merge_sort(L[mid_idx:])

    return merge(low, high)

if __name__ == '__main__':
    case1 = [99, 44, 66, 2, 3, 7, 1, 19, 33, 88]
    
    print(f'before: {case1}')
    res = merge_sort(case1)
    print(f'after: {res}')

    case2 = [99, 44, 66, 2, 3, 7, 1, 19, 33, 88, -1]
    
    print(f'before: {case2}')
    res = merge_sort(case2)
    print(f'after: {res}')
