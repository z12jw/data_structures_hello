import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree

class BinarySearchTree:
    """二叉搜索树"""

    def __init__(self):
        """构造方法"""
        # 初始化空树
        self._root = None
    
    def get_root(self) -> TreeNode | None:
        """获取二叉树根节点"""
        return self._root
    
    def search(self, num: int)-> TreeNode | None:
        """查找节点"""
        cur = self._root
        while cur is not None:
            # 目标节点在右子树
            if cur.val < num:
                cur = cur.right
            # 目标节点在左子树
            elif cur.val > num:
                cur = cur.left
            # 找到目标节点，跳出循环
            else:
                break
        return cur
    
    def insert(self, num: int):
        """插入节点"""
        # 若树为空，则初始化根节点
        if self._root == None:
            self._root = TreeNode(num)
            return
        # 用两个节点来表示本身和父节点
        cur, pre = self._root,None
        #cur超过叶节点退出
        while cur is not None:
            #有相同节点值就退出
            if cur.val == num:
                return
            # 先确定cur的父节点
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left
        # 找到插入位置的父节点,并插入
        node = TreeNode(num)
        if pre.val > num:
            pre.left = node
        else:
            pre.right = node
    
    def remove(self, num: int):
        """删除节点"""
        #若树为空，直接返回
        if self._root == None:
            return
        
        # 循环查找，cur来记录删除节点,pre是其父节点
        cur ,pre = self._root,None
        while cur is not None:
            #找到删除的节点退出循环
            if cur.val == num:
                break
            pre = cur
            if cur.val < num:
                cur = cur.right
            elif cur.val > num:
                cur = cur.left
        #没有找到要删除的节点
        if cur is None:
            return
        
        #cur的度为0/1
        if cur.left is None or cur.right is None:
            #子节点来代替删除的节点
            child = cur.left or cur.right  #优先取 cur.left，如果它是“假值”（通常是 None），就取 cur.right
            if cur is not self._root:
                if pre.right == cur:
                    pre.right = child
                else:
                    pre.left = child
            #删除的是根节点
            else:
                self._root = child
        
        #cur的度为2
        else:
            #用中序遍历cur节点的后一位来代替删除节点,即cur的右子树的最左下的节点tmp
            tmp : TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            #递归删除节点tmp
            self.remove(tmp.val)
            #用tmp的值覆盖cur的值
            cur.val = tmp.val
            
        
        
if __name__ == '__main__':
    #初始化二叉搜索树
    bst = BinarySearchTree()
    nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # 请注意，不同的插入顺序会生成不同的二叉树，该序列可以生成一个完美二叉树
    for num in nums:
        bst.insert(num)
    print("\n初始化的二叉树为\n")
    print_tree(bst.get_root())

    # 查找节点
    node = bst.search(15)
    print("\n查找到的节点对象为: {}，节点值 = {}".format(node, node.val))
    
    # 插入节点
    bst.insert(16)
    print("\n插入节点 16 后，二叉树为\n")
    print_tree(bst.get_root())
    
    # 删除节点
    bst.remove(1)
    print("\n删除节点 1 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(2)
    print("\n删除节点 2 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(8)
    print("\n删除节点 4 后，二叉树为\n")
    print_tree(bst.get_root())