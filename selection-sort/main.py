def selection_sort(L):
    start = 0
    while start < len(L):
        for i in range(start, len(L)):
            if L[i] < L[start]:
                L[i], L[start] = L[start], L[i]
        start += 1
    return L

if __name__ == '__main__':
    case1 = [9,5,2,8,4,3,7,6,1,10,-1,0]

    print(f'before: {case1}')
    res = selection_sort(case1)
    print(f'after: {res}')
