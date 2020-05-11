def trapping_rain(buildings):
    # 코드를 작성하세요
    trapped_rain = 0 #물에 잠긴 칸 수
    max_val = max(buildings) # 가장 높은 빌딩의 칸
    """
    가장 높은 빌딩의 칸까지 물을 채운 뒤에 층마다 물이 남아있을 수 있는 조건인지 검사하여 제거합니다.
    """
    for i in range(len(buildings)):
        trapped_rain += max_val - buildings[i]
    # 가장 높은 층부터 시작해서 1층까지 내려가며 검사합니다.
    for i in range(max_val, 0 ,-1):
        temp = []
        # 해당하는 층의 모든 가로칸을 검사합니다.
        for j in range(len(buildings)):
            if i <= buildings[j]:
                temp.append(j)
        # 만약 해당하는 층에 빌딩이 한 칸 있다면, 그 층의 물은 모두 제거됩니다.
        if len(temp) == 1:
            trapped_rain -= (len(buildings)-len(temp))
        # 해당 층에 빌딩이 두칸 이상 있다면, 리스트의 시작부터 처음의 빌딩까지, 마지막의 빌딩에서 리스트의 끝까지의 칸에
        #       해당하는 물을 제거합니다.
        elif len(temp) > 1:
            trapped_rain -= temp[0]
            trapped_rain -= (len(buildings)-(temp[-1]+1))
    return  trapped_rain
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))