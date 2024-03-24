def bubble_sort(L):
    do_swap = True
    while do_swap:
        do_swap = False
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                do_swap = True
                tmp = L[i]
                L[i] = L[i-1]
                L[i-1] = tmp
    return L

if __name__ == '__main__':
    test_case_1 = [99, 44, 66, 2, 3, 7, 1, 19, 33, 88]

    print(f'before: {test_case_1}')
    res = bubble_sort(test_case_1)
    print(f'final sorted: {res}')