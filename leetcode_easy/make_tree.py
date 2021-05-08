class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# list = [1,2,3,4,5,6,7]

# node = TreeNode(list)
# node.root = list[0]

# for i,v in enumerate(list[1:]):
#     if i%2 == 1:
#         node.left = v
#     else:
#         node.right = v
#print(node)



class Solution(object):
    def createnode(self,x):
        node = TreeNode(x)
        print('1 > ',node)
        for i in range(1,len(x)):      

            if i %2 == 1:
                node.left = x[i]
            else:
                node.right = x[i]
        print('2 > ',node)




#make binary tree
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None

        
# class BinarySearchTree(object):

#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         self.root = self._insert_value(self.root, data)
#         return self.root is not None
#     def _insert_value(self, node, data):
#         if node is None:
#             node = Node(data)
#         else:
#             if data <= node.data:
#                 node.left = self._insert_value(node.left, data)
#             else:
#                 node.right = self._insert_value(node.right, data)
#         return node

# bst = BinarySearchTree()
# array = [6,9,7,5]
# for x in array:
#     bst.insert(x)
#     print(bst.insert(x))
#########    




        

s = Solution()
print(s.create([1,2,3,4,5,6,7]))       