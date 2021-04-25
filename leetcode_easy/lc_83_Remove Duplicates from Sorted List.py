"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None:
            return head
        t = head.next
        p = head
        
        while t !=None:
            if p.val == t.val:                
                p.next = t.next
                t = t.next

            else:
                t = t.next
                p = p.next
                
        return head
    

s = Solution()
print(s.deleteDuplicates([1,1,2]))
#print(s.deleteDuplicates([1,1,2,3,3]))
#print(s.deleteDuplicates(5))         


