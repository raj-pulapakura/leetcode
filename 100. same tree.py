# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p and q

        q1, q2 = [p], [q]

        while len(q1) != 0 or len(q2) != 0:
            if len(q1) != len(q2): return False

            v1 = q1.pop()
            v2 = q2.pop()
            if not v1 and not v2: continue
            if (not v1 and v2) or (v1 and not v2): return False
            if v1.val != v2.val: return False
            if v1 and (v1.left or v1.right):
                q1.insert(0, v1.left)
                q1.insert(0, v1.right)
            if v2 and (v2.left or v2.right):
                q2.insert(0, v2.left)
                q2.insert(0, v2.right)

        return True
    
    def isSameTreeDFS(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(pn: TreeNode, qn: TreeNode):
            if not pn or not qn:
                return pn is None and qn is None
            
            if pn.val != qn.val: return False

            leftSame = dfs(pn.left, qn.left)
            rightSame = dfs(pn.right, qn.right)

            return leftSame and rightSame
            

        return dfs(p, q)
    
print(Solution().isSameTreeDFS(TreeNode(1, left=TreeNode(2), right=TreeNode(3)), TreeNode(1, left=TreeNode(2), right=TreeNode(3))))