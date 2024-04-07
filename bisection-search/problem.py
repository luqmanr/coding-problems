"""
search an element in a List by picking the middle point
if element == middle point
    return Found
if element < middle point
    search through lower half of List
if element > middle point
    search through upper half of List

do this recursively until the element is found
or if element is not in List, then return Not Found
"""
def bisection_search(L, e):
    pass

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