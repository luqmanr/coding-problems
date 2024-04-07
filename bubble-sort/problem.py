"""
iterate over a list
if the current element is smaller than the next element
    swap the elements
then do it again from the start of the list
until no swap happens, then that means
the list is sorted
"""
def bubble_sort(L):
    pass

if __name__ == '__main__':
    test_case_1 = [99, 44, 66, 2, 3, 7, 1, 19, 33, 88]

    print(f'before: {test_case_1}')
    res = bubble_sort(test_case_1)
    print(f'final sorted: {res}')

    test_case_2 = [99, 44, 66, 2, -3, 7, 1, -19, 33, 88]

    print(f'before: {test_case_2}')
    res = bubble_sort(test_case_2)
    print(f'final sorted: {res}')