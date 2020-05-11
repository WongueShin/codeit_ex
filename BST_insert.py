class Node:
    """이진 탐색 트리 노드 클래스"""

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 코드를 쓰세요
        if data > self.root.data:
            if self.root.right_child is None:
                self.root.right_child = new_node
                new_node.parent = self.root
                return
            else:
                iterator = self.root.right_child
        else:
            if self.root.left_child is None:
                self.root.left_child = new_node
                new_node.parent = self.root
                return
            else:
                iterator = self.root.left_child
        while iterator is not None:
            if data > iterator.data:
                if iterator.right_child is None:
                    iterator.right_child = new_node
                    new_node.parent = iterator
                    return
                else:
                    iterator = iterator.right_child
            else:
                if iterator.left_child is None:
                    iterator.left_child = new_node
                    new_node.parent = iterator
                    return
                else:
                    iterator = iterator.left_child


    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()
