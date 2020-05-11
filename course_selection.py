def course_selection(course_list):
    # 코드를 작성하세요.
    if len(course_list) == 0:
        return []
    else:
        temp = []
        for i in range(len(course_list)):
            temp.append(course_list[i][-1])
        out_val = course_list[temp.index(min(temp))]
        # print(out_val)
        course_list.remove(out_val)
        temp = []
        cache = 0
        for j in range(len(course_list)):
            if course_list[j - cache][0] < out_val[1]:
                course_list.remove(course_list[j - cache])
                cache += 1

        return [out_val] + course_selection(course_list)


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
