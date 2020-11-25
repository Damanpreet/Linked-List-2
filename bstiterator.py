# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Space complexity - O(n) to keep all nodes in the nodes_sorted array + O(h) for the recursive stack.
# Did this solution run on leetcode? - yes
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.ptr = -1
        self.__inorder(root)
    
    def __inorder(self, node) -> None:
        """
        Function to get the inorder traversal of nodes.
        # Time complexity - O(n) visits all nodes
        """
        if node:
            self.__inorder(node.left)
            self.nodes_sorted.append(node.val)
            self.__inorder(node.right)
            
    def next(self) -> int:
        """
        @return the next smallest number
        # Time complexity - O(1) gets the node value using the pointer
        """
        if self.ptr < len(self.nodes_sorted):
            self.ptr += 1
            return self.nodes_sorted[self.ptr]
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        # Time complexity - O(1) checks if the ptr is less than the size of the array.
        """
        return self.ptr < len(self.nodes_sorted)-1


# CONTROLLED RECURSION
# Space complexity - O(h)
# Did this solution run on leetcode? - yes
from collections import deque
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes = deque()
        self.__leftinorder(root)
        
    def __leftinorder(self, node):
        """
        Traverse the left nodes
        """
        while node:
            self.nodes.append(node)
            node = node.left
    
    def next(self) -> int:
        """
        @return the next smallest number
        Time complexity - O(1) --> at max. need to traverse h nodes
        """
        if len(self.nodes) > 0:
            curr_node = self.nodes.pop()
            self.__leftinorder(curr_node.right)   # add the left subtree of the right child.
            return curr_node.val
    
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        Time complexity - O(1) 
        """
        return len(self.nodes)!=0
    
    
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
