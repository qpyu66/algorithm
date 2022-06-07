"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.

"""


#runtime 32 ms
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split()
        #print(sp,len(sp))        
        if (len(sp) == 0):
            #print('not')
            return 0
        else:
            return len(sp[-1])

#runtime 16 ms 
#code refactor
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.split()
#         for i in words:
#             i.strip()
#         if words == []:
#             return 0
#         return len(words[-1])

        
s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord(" "))
print(s.lengthOfLastWord("Hello World si"))
print(s.lengthOfLastWord("       "))