# 퀵 정렬에서 사용되는 partition 함수
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index2]
    my_list[index2] = my_list[index1]
    my_list[index1] = temp
    return my_list

def partition(my_list, start, end):
    # 코드를 작성하세요.
    pivot = end
    p_val = my_list[pivot]
    big_g = start
    small_g = start-1
    for i in range(end-start):
        if my_list[i] > p_val:
            big_g = i
        else:
            swap_elements(my_list,small_g+1,i)
            small_g += 1
            big_g = i
    swap_elements(my_list,small_g+1,pivot)
    return  small_g+1

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
