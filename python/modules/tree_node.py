from collections import deque

class TreeNode:
    """二叉树节点类"""
    
    def __init__(self,val:int):
        self.val = val # 节点值
        self.height : int = 0 # 树高度
        self.left : TreeNode | None = None # 左子节点引用
        self.right : TreeNode |None = None # 右节点
        
def list_to_tree_bfs(arr: list[int],i:int)-> TreeNode | None:
    """将列表反序列化为二叉树：递归"""
    # 如果索引超出数组长度，或者对应的元素为 None ，则返回 None
    if i < 0 or i >= len(arr) or arr[i] == None:
        return None
    
    # 构造当前节点
    node = TreeNode(arr[i])
    #递归左右子树
    node.left = list_to_tree_bfs(arr,2*i +1)    
    node.right = list_to_tree_bfs(arr, 2*i+2)
    return node

def list_to_tree(arr:list[int]) -> TreeNode | None:
    """将列表反序列化为二叉树"""
    return list_to_tree_bfs(arr,0)

def tree_to_list_bfs(root: TreeNode, i: int ,res: list[int]) ->list[int]:
    """将二叉树序列化为列表：递归"""
    if root is None:
        return
    # 列表增加长度= 目标长度 - 实际长度
    if i >= len(res):
        res += [None]*(i + 1 - len(res))
    res[i] = root.val
    # 递归 进列表
    tree_to_list_bfs(root.left,2*i + 1,res)
    tree_to_list_bfs(root.right,2*i + 2,res)

def tree_to_list(root: TreeNode)-> list[int]:
    res =[]
    tree_to_list_bfs(root,0,res)
    return res