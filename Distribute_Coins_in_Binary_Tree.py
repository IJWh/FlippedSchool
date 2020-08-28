# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(cur_node):
            L = dfs(cur_node.left) if cur_node.left else 0
            R = dfs(cur_node.right) if cur_node.right else 0
            
            self.result += abs(L) + abs(R)
            return cur_node.val + L + R - 1

        dfs(root)
        return self.result
        
# 동전의 수 = Node의 수
# Node에 할당된 동전의 값이 1이 아니라면 
#   0 이라면: 어디선가 가져와야한다
#   2 이상이라면: 어디론가 보내야한다
# dfs방식으로 필요한 이동횟수를 leaf에서부터 root까지 누적
