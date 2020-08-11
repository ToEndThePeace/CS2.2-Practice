class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree_(root):
    if root is None:
        return True
    if root.left and root.value <= root.left.value:
        return False
    if root.right and root.value >= root.right.value:
        return False
    return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)
