from .tree_node import TreeNode, list_to_tree

class Trunk:
    def __init__(self, prev, string: str | None = None):
        self.prev = prev
        self.str = string


def show_trunks(p: Trunk | None):
    if p is None:
        return
    show_trunks(p.prev)
    print(p.str, end="")


def print_tree(
    root: TreeNode | None, prev: Trunk | None = None, is_right: bool = False
):
    """
    打印二叉树
    """
    if root is None:
        return

    prev_str = "    "
    trunk = Trunk(prev, prev_str)
    print_tree(root.right, trunk, True)

    if prev is None:
        trunk.str = "———"
    elif is_right:
        trunk.str = "/———"
        prev_str = "   |"
    else:
        trunk.str = "\———"
        prev.str = prev_str

    show_trunks(trunk)
    print(" " + str(root.val))
    if prev:
        prev.str = prev_str
    trunk.str = "   |"
    print_tree(root.left, trunk, False)
