# Kamesh Vedula
# Problem: Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def rightSideView(self, root: TreeNode) -> List[int]:
    if root is None:
        return []

#         q = []
#         q.append(root)
#         levelOrder = []

#         while q:
#             count = len(q)
#             level = [] 
        
#             for i in range(count):
#                 temp = q.pop(0)
#                 level.append(temp.val)
            
#                 if temp.right:
#                     q.append(temp.right)
#                 if temp.left:
#                     q.append(temp.left)

#             levelOrder.append(level)
        
#         rightVals = [lvl[-1] for lvl in levelOrder]
#         return rightVals


    q = collections.deque()
    q.append(root)
    levelOrder = []
    
    while q:
        count = len(q)
        
        for i in range(count):
            temp = q.popleft()
            
            if i == 0:
                levelOrder.append(temp.val)
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)

    return levelOrder


