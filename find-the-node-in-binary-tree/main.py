# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # if original input is null, return
        # if target is null, return
        if original is None or target is None:
            return None
        
        # init queue
        queue = []
        
        # pass in first node of BT to traverse
        queue.append(cloned)
        
        # traverse queue
        # while queue is not empty
        while(len(queue) > 0):
            # get the first node in the queue
            # and remove from queue
            node = queue.pop(0)
            
            # if the value is the same as target, return found node
            if node.val == target.val:
                return node
            
            # add left and right node, if not None
            if node.left is not None:
                queue.append(node.left)
                
            if node.right is not None:
                queue.append(node.right)
        
        return None