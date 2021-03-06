# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root == None:
            return "None"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = data.split(",")
        root = self.bbuildTree(data)
        return root

    def bbuildTree(self, arr):
        if len(arr) == 0:
            return
        item = arr.pop(0)
        root = None
        if item != "None":
            root = TreeNode(item)
            root.left = self.bbuildTree(arr)
            root.right = self.bbuildTree(arr)
        return root

    # Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans