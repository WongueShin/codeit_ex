def min_coin_count(value, coin_list):
    # 코드를 작성하세요.
    output = 0
    coin_list.sort(reverse= True)
    #print('coin_list= '+str(coin_list))
    while value > 0:
        for i in range(len(coin_list)):
            if value//coin_list[i] > 0:
                output += value//coin_list[i]
                #print('output= '+str(output))
                value = value % coin_list[i]
                #print('value= '+str(value))
            else:
                pass
    return output
# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))