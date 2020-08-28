# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        result = []
        
        if not root:
            return result
        
        def r_node_val(cur_node:TreeNode):
            cur_node.val *= -1
            if cur_node.left is not None:
                r_node_val(cur_node.left)
            if cur_node.right is not None:
                r_node_val(cur_node.right)
            
            
        
        def each_path(cur_node: TreeNode, prev_path:List[int]):
            cur_path = copy.deepcopy(prev_path)
            cur_path.append(cur_node.val)
            
            # leaf까지 도착
            if cur_node.left is None and cur_node.right is None:
                cur_total = sum(cur_path)
                # sum값도 일치한 경우
                if cur_total == total:
                    result.append(cur_path)
                    
            # 더 내려갈수 있을 경우
            else:
                if cur_node.left is not None:
                    each_path(cur_node.left, cur_path)
                if cur_node.right is not None:
                    each_path(cur_node.right, cur_path)
                    
            return
            
        r_val = False
        if total < 0:
            r_node_val(root)
            total *= -1
            r_val = True
            
        each_path(root,[])
        
        if r_val:
            for i in range(len(result)):
                for j in range(len(result[i])):
                    result[i][j] *= -1
        return result
