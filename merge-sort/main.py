"""
divide a list until it is of length 1
then sort and merge each 2 list to each other
by comparing each items in the list
then do it recursively until we get the final list
"""
def merge_sort(L):
    """
    iterate over two sorted list
    compare each element in the list each iteration,
    until one of the list is at the end
    then copy the rest
    """
    def merge(low, high):
        i = 0
        j = 0

        result = []
        while i < len(low) and j < len(high):
            if low[i] < high[j]:
                result.append(low[i])
                i += 1
            else:
                result.append(high[j])
                j += 1
        
        while i < len(low):
            result.append(low[i])
            i += 1

        while j < len(high):
            result.append(high[j])
            j += 1
        
        return result
    
    if len(L) == 1:
        return L
    
    mid = len(L) // 2
    low = merge_sort(L[:mid])
    high = merge_sort(L[mid:])
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
