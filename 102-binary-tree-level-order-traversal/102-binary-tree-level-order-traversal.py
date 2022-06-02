# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        
        res = []
        
        def helper(node, level):
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                helper(node.left, level + 1)
                helper(node.right, level + 1)
        
        helper(root, 0)
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        levels = []

        def helper(node, level):
            if node:
                if len(levels) == level:
                    levels.append([])
                levels[level] += [node.val]
                helper(node.left, level+1)
                helper(node.right, level+1)

        helper(root, 0)
        return levels
    
    
    
    
    