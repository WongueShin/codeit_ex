def merge(list1, list2 ):
    # 코드를 작성하세요.
    temp = []
    if len(list1) != 0 and len(list2) != 0 :
        condition = True
        while condition == True:
            if list1[0] > list2[0]:
                temp.append(list2[0])
                list2 = list2[1:]
            else:
                temp.append(list1[0])
                list1 = list1[1:]
            if len(list1) == 0 or len(list2) == 0:
                condition = False
    if len(list1) > 0:
        temp += list1
    elif len(list2) >0:
        temp += list2
    return temp

def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) > 1:
       # print('list~0.5: '+ str(my_list[:len(my_list)//2]))

        return merge(merge_sort(my_list[:len(my_list)//2]), merge_sort(my_list[len(my_list)//2:]))
    else:
        return my_list

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
#print('end')
