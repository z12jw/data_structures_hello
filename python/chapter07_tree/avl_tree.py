import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree

class AVLTree:
    """AVL 树"""
    
    def __init__(self):
        """构造方法"""
        self._root = None
    
    def get_root(self) -> TreeNode | None:
        """获取二叉树节点"""
        return self._root
    
    def height(self, node: TreeNode|None):
        """获取节点高度"""
        # 空节点高度-1，叶节点高度0
        if node is not None:
            return node.height
        return -1
    
    def update_height(self, node: TreeNode | None):
        """更新节点高度"""
        # 节点高度等于子树高度 +1
        node.height = max([self.height(node.height), self.height(node.right)]) + 1
        
    def balance_factor(self, node: TreeNode | None) -> int:
        """获取平衡因子"""
        if node is None:
            return 0
        #节点平衡因子 = 左子树 - 右子树
        return self.height(node.left) - self.height(node.right)
    
    