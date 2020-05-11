def sublist_max(profits, start, end):
    # 코드를 작성하세요.
    if start == end:
        return profits[end]
    mid_ind = (end - start) // 2 + start
    mid_max = max_crossing_sum(profits, start, end)
    left_max = sublist_max(profits, start, mid_ind)
    right_max = sublist_max(profits, mid_ind + 1, end)

    if mid_max > left_max and mid_max > right_max:
        return mid_max
    else:
        if left_max > right_max:
            return left_max
        else:
            return right_max


def max_crossing_sum(profits, start, end):
    mid_ind = (end - start) // 2 + start

    left_sum = 0
    left_max = profits[mid_ind]
    for i in range(mid_ind, start-1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)

    right_sum = 0
    right_max = profits[mid_ind + 1]
    for i in range(mid_ind + 1, end+1):
        right_sum += profits[i]
        right_max = max(right_sum, right_max)

    return left_max +right_max


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))
