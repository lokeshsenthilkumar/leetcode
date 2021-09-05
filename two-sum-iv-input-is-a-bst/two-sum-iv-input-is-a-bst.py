# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        st = set()
        
        def helper(root,k):
        
            if not root:
                return False

            if k - root.val in st:
                return True

            st.add(root.val)

            return helper(root.left,k) or helper(root.right,k)
        
        return helper(root,k)