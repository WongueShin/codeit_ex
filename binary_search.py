def binary_search(element, some_list):
    # 코드를 작성하세요.
    stat = True
    temp = 0
    #print('ele= ' + str(element))
    while (stat == True):
        target = int(len(some_list)/2)
        #print('target= ' + str(target))

        if target == 0 :
            if element == some_list[target]:
                return temp+target
            return None
        if element == some_list[target]:
            return target+temp
        elif element >= some_list[target]:
            some_list = some_list[target:]
            temp += target
        else:
            some_list = some_list[ :target]


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))