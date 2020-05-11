
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index2]
    my_list[index2] = my_list[index1]
    my_list[index1] = temp
    return my_list

# 이전 과제에서 작성한 코드를 붙여 넣으세요!


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    pivot = end
    p_val = my_list[pivot]
    big_g = start
    small_g = start - 1
    for i in range(end - start):
        if my_list[i] > p_val:
            big_g = i
        else:
            swap_elements(my_list, small_g + 1, i)
            small_g += 1
            big_g = i
    swap_elements(my_list, small_g + 1, pivot)
    return small_g + 1


# 이전 과제에서 작성한 코드를 붙여 넣으세요!


# 퀵 정렬
def quicksort(my_list, start= False, end= False):
    if start == False:
        start = 0
    if end == False:
        end = len(my_list)-1
    pivot = partition(my_list,start,end)
    #print('pivot= '+str(pivot))
    my_list[:pivot] = sorted(my_list[:pivot])
    my_list[pivot:] = sorted(my_list[pivot:])



# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)
# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)