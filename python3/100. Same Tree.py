# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True 
        if not p or not q: return False

        stack = [p, q]
        while stack:
            if len(stack) < 2:
                return False
            q = stack.pop()
            p = stack.pop()
            if p is None and q is None:
                continue
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                print(p.val, q.val)
                return False
            else:
                stack.append(p.right)
                stack.append(q.right)
                stack.append(p.left)
                stack.append(q.left)

        return True
 
