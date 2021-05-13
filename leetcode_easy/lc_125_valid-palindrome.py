"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word1 = ''.join(re.findall("[a-zA-Z0-9]+",s))
        
        lowword = word1.lower()
        
        if lowword == lowword[::-1]:
            return True
        else:
            return False


#code refactoring
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]",'', s.lower())
        return s == s[::-1]




s = Solution()
#print(s.isPalindrome("A man, a plan, a canal: Panama"))        
#print(s.isPalindrome("race a car"))    
print(s.isPalindrome("0P"))   
