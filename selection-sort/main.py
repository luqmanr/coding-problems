def selection_sort(L):
    suffixSt = 0
    while suffixSt < len(L):
        for i in range(suffixSt, len(L)):
            # print(i, suffixSt)
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
        print(L)
    return L

if __name__ == '__main__':
    case1 = [9,5,2,8,4,3,7,6,1,10,-1,0]

    print(f'before: {case1}')
    res = selection_sort(case1)
    print(f'after: {res}')
