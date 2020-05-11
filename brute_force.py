# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기 코드를 쓰세요
    temp = [distance(coordinates[0], coordinates[1]), 0, 0]
    for a in range(0, len(coordinates) - 2):
        for b in range(a + 1, len(coordinates) - a):
            resulte = distance(coordinates[a], coordinates[b])
            if temp[0] > resulte:
                temp[0] = resulte
                temp[1] = coordinates[a]
                temp[2] = coordinates[b]
    return [temp[1], temp[2]]


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
