"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sn = s.split(' ')
        par = []
        dic={}
        answer = True
        
        for p,s in zip(pattern,sn):
            print(p,s)
            if p not in dic.keys():
                dic[p] = s
            else:
                if dic[p] != s :
                    return False
                
        if(len(set(dic.keys())) != len(set(dic.values())) or len(pattern) != len(sn)):
            return False
        return True
         
        
#code refactoring
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if pattern[i] not in d:
                d[pattern[i]] = s[i]
            else:
                if d[pattern[i]] != s[i]:
                    return False
        if len(set(d.values())) != len(d.keys()):
            return False
        return True
        

#code refactoring
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        cache = {}
        words = s.split(" ")
        if len(words) != len(pattern): return False
        
        if len(set(pattern)) != len(set(words)): return False
        
        for j in range(len(words)):
            if pattern[j] in cache:
                if cache[pattern[j]] != words[j]: return False
            
            else:
                cache[pattern[j]] = words[j]
                
        return True

        
s = Solution()
# print(s.wordPattern("abba","dog cat cat dog"))        
# print(s.wordPattern("abba","dog cat cat fish"))        
print(s.wordPattern("aba","cat cat cat dog"))        



