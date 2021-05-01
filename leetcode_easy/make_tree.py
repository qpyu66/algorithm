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
        

s = Solution()
print(s.create([1,2,3,4,5,6,7]))       