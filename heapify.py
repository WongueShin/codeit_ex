def swap(tree: object, index_1: object, index_2: object) -> object:
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 코드를 쓰세요.
    if left_child_index > tree_size:
        left_child = None
    else:
        left_child = tree[left_child_index]

    if right_child_index > tree_size:
        right_child = None
    else:
        right_child = tree[right_child_index]

    if left_child and right_child is not None:
        val_list = [tree[index], left_child, right_child]
        #print(val_list)
        max_val = max(val_list)
        max_ind = tree.index(max_val)
        #print(max_val)
        #print(max_ind)
        swap(tree, index, max_ind)
        heapify(tree, max_ind, tree_size)

    elif left_child is not None and right_child is None:
        val_list = [tree[index], left_child]
        max_val = max(val_list)
        swap(tree, index, val_list.index(max_val))
        return None
    else:
        return None



# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
#print(tree)
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
"""for i in range(2,len(tree)-1):
    print(i)
    heapify(tree,i,len(tree))"""
print(tree)