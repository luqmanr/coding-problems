"""
divide a list until it is of length 1
then sort and merge each 2 list to each other
by comparing each items in the list
then do it recursively until we get the final list
"""
def merge_sort(L):
    pass
    
if __name__ == '__main__':
    case1 = [99, 44, 66, 2, 3, 7, 1, 19, 33, 88]
    
    print(f'before: {case1}')
    res = merge_sort(case1)
    print(f'after: {res}')

    case2 = [99, 44, 66, 2, 3, 7, 1, 19, 33, 88, -1]
    
    print(f'before: {case2}')
    res = merge_sort(case2)
    print(f'after: {res}')
