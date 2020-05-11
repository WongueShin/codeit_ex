def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    for i in range(len(sorted_list) - 1, 0, -1):
        temp = sorted_list[i]
        temp_list = sorted_list[:i]
        mid_val = temp_list[len(temp_list) // 2]
        #print(f'mid val ={mid_val}\n sorted_list ={sorted_list}')
        while len(temp_list) > 2:
            if mid_val + temp == search_sum:
                return True

            if mid_val + temp > search_sum:
                temp_list = temp_list[:temp_list.index(mid_val)]
                mid_val = temp_list[len(temp_list) // 2]
                #print(f'mid val ={mid_val}\n temp_list ={temp_list}')

            if mid_val + temp < search_sum:
                temp_list = temp_list[temp_list.index(mid_val):]
                mid_val = temp_list[len(temp_list) // 2]
                #print(f'mid val ={mid_val}\n temp_list ={temp_list}')
        for j in temp_list:
            if j == search_sum:
                return True
        #print(f'can`t find in val = {i}')
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
