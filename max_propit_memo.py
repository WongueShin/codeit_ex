def max_profit_memo(price_list, count, cache):
    # 코드를 작성하세요.
    '''
            **** base case ***
    '''
    # 공간 복잡도를 위해, 0개와 1개를 팔아야 할 경우의 수가 필요하지 않으면 딕셔너리에 기록되지 않게 했습니다.
    if count == 0:
        cache[0] = 0
        return cache[0]
    if count == 1:
        cache[1] = 100
        return cache[1]
    # 캐쉬 안에 저장된 값이 있을 경우, 바로 호출하여 사용할 수 있도록 합니다.
    if count in cache:
        return cache[count]

    '''
        ***Recursive case***
    '''
    val_list = []   # 캐쉬 안에 새로운 값을 기입하기 이전에, MAX값을 추출 할 수 있도록 값을 임시로 들고있게 합니다.

    # 만약, count값이 list의 길이보다 적어, 리스트 후반에 들어있는 값을 사용하지 말아야 할 경우에 대비해서 이중 for문을 써, 조건에 맞지 않으면 돌아가지 않도록 했습니다.
    # i는 한번에 얼마나 크게 묶어서 팔 수 있는지(price_list의 n번째 값까지 사용 가는한지)에 대한 변수입니다.
    for i in range(len(price_list)-1,0,-1):

        # j 의 값의 의미는 price_list의 값을 몇단위로 팔수 있는지에 대한 변수입니다. len(list)보다 count가 클 경우에도 코드가 성립하기 위해서.
        for j in range(count//i,0,-1):
            temp = price_list[i]*j + max_profit_memo(price_list, count-(j*i), cache)
            val_list.append(temp)
    # print(f' print_list ={price_list}\n count= {count}\n cache= {cache}')  # test code
    cache[count] = max(val_list)    # 가능한 경우의 수를 재귀적으로 계산 한 뒤 최댓값을 뽑아 캐쉬에 기입합니다.
    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))