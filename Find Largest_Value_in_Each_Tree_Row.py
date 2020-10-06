# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.largest_val = [None]*10*10*10*10
        
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        
        def update_val(n:TreeNode, depth:int):
            if self.largest_val[depth] is None:
                self.largest_val[depth] = n.val
            else:
                self.largest_val[depth] = max(self.largest_val[depth], n.val)
            
            if n.left is not None:
                update_val(n.left, depth+1)
            if n.right is not None:
                update_val(n.right, depth+1)
                
        
        update_val(root,0)
        
        for val in self.largest_val[:]:
            if val is None:
                self.largest_val.remove(None)
        
        return self.largest_val
