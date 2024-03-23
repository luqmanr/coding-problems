def bubble_sort(list):
    do_swap = True
    n = 1
    while do_swap is True:
        print(f'iteration num: {n}')
        n += 1
        do_swap = False
        for j in range(1, len(list)):
            if list[j-1] > list[j]:
                do_swap = True
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
            print(list)

if __name__ == '__main__':
    test_list = [1,5,23,2,9,7,18,13,4,6,99,77]
    bubble_sort(test_list)