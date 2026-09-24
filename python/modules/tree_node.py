from collections import deque

class TreeNode:
    """二叉树节点类"""
    
    def __init__(self,val:int):
        self.val = val # 节点值
        self.left = TreeNode | None = None # 左子节点引用
        self.right = TreeNode |None = None # 右节点