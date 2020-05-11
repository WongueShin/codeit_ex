# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    cache = {}
    return compute(stairs, possible_steps, cache)


def compute(stairs, possible_steps, cache):
    if stairs in cache:
        return cache[stairs]

    if stairs > possible_steps[2]:
        return_val = compute(stairs - possible_steps[0],possible_steps, cache) + compute(stairs - possible_steps[1],possible_steps, cache) + compute(
            stairs - possible_steps[2],possible_steps, cache)
        cache[stairs] = return_val
        return return_val

    if stairs == possible_steps[2]:
        return_val = compute(stairs - possible_steps[0],possible_steps, cache) + compute(stairs - possible_steps[1],possible_steps, cache) + 1
        cache[stairs] = return_val
        return return_val

    if possible_steps[2] > stairs > possible_steps[1]:
        return_val = compute(stairs - possible_steps[0],possible_steps, cache) + compute(stairs - possible_steps[1],possible_steps, cache)
        cache[stairs] = return_val
        return return_val

    if stairs == possible_steps[1]:
        return_val = compute(stairs - possible_steps[0],possible_steps, cache) + 1
        cache[stairs] = return_val
        return return_val

    if possible_steps[1] > stairs > possible_steps[0]:
        return_val = compute(stairs - possible_steps[0],possible_steps, cache)
        cache[stairs] = return_val
        return return_val

    if stairs <= possible_steps[0]:
        return_val = 1
        cache[stairs] = return_val
        return return_val


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
