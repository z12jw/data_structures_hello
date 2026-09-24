import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree, print_tree

def pre_order(root:TreeNode | None):
    """前序遍历"""
    if root is None:
        return
    # 根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)
    
def in_order(root:TreeNode | None):
    """中序遍历"""
    if root is None:
        return
    #左子树 -> 根节点 -> 右子树
    in_order(root.left)
    res.append(root.val)
    in_order(root.right)
    
def post_order(root:TreeNode | None):
    """"后序遍历"""
    if root is None:
        return
    # 左子树 -> 右子树 -> 根节点
    post_order(root.left)
    post_order(root.right)
    res.append(root.val)

if __name__ == '__main__':
    root = list_to_tree(arr = [1,2,3,4,5,6,7,8])
    print('初始化二叉树')
    print_tree(root)
    
    res = []
    pre_order(root)
    print("前序遍历：", res)
    
    res.clear()
    in_order(root)
    print('中序遍历：', res)
    
    res.clear()
    post_order(root)
    print('后序遍历：', res)