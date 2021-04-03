"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

"""


class Solution:
    def isValid(self, s: str) -> bool:
        slist = list(s)
        slen = len(slist)       
        an =[]        

        if len(s) % 2 !=0:
            return False
        if len(s) == 0:
            return False
        
        for i in range(0,slen):
            if slist[i] in ['(','{','['] :
                an.append(slist[i])
            else:
                if slist[i] == ')' and an.pop() !='(' :   
                    return False
                elif slist[i] == '}' and an.pop() !='{' :   
                    return False
                elif slist[i] == ']' and an.pop() !='[' :   
                    return False
        return True
    
s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("(("))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
