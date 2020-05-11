def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    if len(some_list) == 0:
        return None

    if some_list[(end_index//2)] == element:
        #print('list= ' + str(some_list))
        #print('ele= ' + str(element))
        return end_index//2
    elif some_list[(end_index//2+1)] == element:
        return end_index//2 + 1

    if some_list[(end_index//2)] >= element:
        return binary_search(element,some_list[:end_index//2])
    else:
        return end_index//2 + binary_search(element,some_list[end_index//2:])

    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))