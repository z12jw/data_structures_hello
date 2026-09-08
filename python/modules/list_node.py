class ListNode:
    """链表节点类"""
    
    def __init__(self,val: int):
        self.val : int = val # 节点值
        self.next: ListNode | None = None # 后继节点引用