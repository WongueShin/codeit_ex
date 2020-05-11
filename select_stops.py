def select_stops(water_stops, capacity):
    # 코드를 작성하세요.
    output_val = []
    remain_water = capacity
    current_location = 0
    while False == (current_location == water_stops[-1]):
        temp = []
        for i in range(len(water_stops)):

            if remain_water - (water_stops[i]-current_location) >= 0:
                #print('in')
                temp.append(water_stops[i])

            else:
                #print('out')
                break

        #print(temp)
        output_val.append(water_stops[water_stops.index(max(temp))])
        current_location = water_stops[water_stops.index(max(temp))]
        #print(current_location)

    return output_val

# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))