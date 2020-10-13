#https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.root:
            return None
        
        n_val = self.root.val
        
        
        if not self.root.left:
            if not self.root.right:
                self.root = None
                return n_val
            self.root=self.root.right
            return n_val
        else:
            def next_small(node: TreeNode):
                # 왼쪽 자식에게 왼쪽자식이 있을경우
                if node.left.left is not None:
                    return next_small(node.left)

                else:
                    # return값은 왼쪽자식의 val값
                    n_val = node.left.val

                    # 왼쪽자식에게 오른쪽자식이 있을경우
                    if node.left.right is not None:
                        # 왼쪽자식을 왼쪽자식의 오른쪽자식으로 갱신
                        node.left = node.left.right

                    else:
                        # 왼쪽자식 삭제
                        node.left = None
                    return n_val
                
            return next_small(self.root)
            
            

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.root:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
