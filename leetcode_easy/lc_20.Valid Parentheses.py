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
        slen = len(s)       
        an =[]
        
        if (len(s) == 0):
            return True
        #입력 받은 str의 개수가 홀수 인 경우
        elif (len(s) % 2 !=0):
            return False
        
        
        for i in range(0,slen):
            #오픈괄호 리스트에 추가
            if (s[i] in ['(','{','['] ):
                an.append(s[i]) 
            else:
                #print("an > ", an, i, len(an))                
                if (len(an) == 0):
                    return False
                #문자와 an에서 마지막의 문자가 같지 않은 경우
                elif (s[i] == ')' and an.pop() !='(') :   
                    return False
                elif (s[i] == '}' and an.pop() !='{') :  
                    return False
                elif (s[i] == ']' and an.pop() !='[') :   
                    return False  
        #for문 끝나고 an안에 개수가 0이 아닌 경우
        if (len(an) != 0):
            return False
        return True
    
s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("(("))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))
 