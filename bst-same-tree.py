# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue1 = []
        queue2 = []
        
        queue1.append(p)
        queue2.append(q)
        
        while queue1 and queue2:
            
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)
            
            #if one node is null and the other is not, we know the trees are not the same
            if (node1 and not node2) or (node2 and not node1):
                return(False)
                        
            else:
                
                #we check and append the queues iff both nodes exist; otherwise, we have reached the end of the trees!
                if node1 and node2:
                
                    if node1.val != node2.val:
                        return(False)

                    queue1.append(node1.left)
                    queue2.append(node2.left)

                    queue1.append(node1.right)
                    queue2.append(node2.right)
                            
        return(True)
            
            
        
        
