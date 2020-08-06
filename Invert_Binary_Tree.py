# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def invert(target):
            if target == None or (target.left == None and target.right == None):
                return
            tmp_node = target.left
            target.left = target.right
            target.right = tmp_node
            
            invert(target.left)
            invert(target.right)
            
        invert(root)
        return root
        
        
