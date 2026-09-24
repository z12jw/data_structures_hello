import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, list_to_tree, print_tree

class ArrayBinaryTree:
    """数组表示下的二叉树类"""
    