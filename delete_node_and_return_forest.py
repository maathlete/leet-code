#question: https://leetcode.com/problems/delete-nodes-and-return-forest/description/

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)

        forest = []

        def delete(root, parent_exists):

            if not root:

                return(None)

            if root.val in to_delete:

                root.left = delete(root.left, parent_exists=False)
                root.right = delete(root.right, parent_exists=False)

                return(None)

            else:

                if not parent_exists:

                    forest.append(root)
                    
                root.left = delete(root.left, parent_exists=True)
                root.right = delete(root.right, parent_exists=True)

                return(root)

        delete(root, parent_exists=False)
        return(forest)
