"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            sarr = s[i]
            tarr = t[i]
            print(sarr, tarr)

            if sarr in sdict and sdict[sarr] != tarr:
                return False
            if tarr in tdict and tdict[tarr] != sarr:
                return False

            sdict[sarr] = tarr
            tdict[tarr] = sarr

        return True



#code refactoring
# class Solution:
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         m = {}
#         mapped = set()  # case "ab", "aa"
#         for i in range(len(s)):
#             if s[i] not in m and t[i] not in mapped:
#                 m[s[i]] = t[i]
#                 mapped.add(t[i])
#             elif s[i] in m and m[s[i]] == t[i]:
#                 pass        
#             else:
#                 return False
#         return True


#code refactoring
# class Solution(object):
#     def isIsomorphic(self, s, t):
#         print(set(zip(s, t)))
#         return len(set(zip(s, t))) == len(set(s)) == len(set(t))


s = Solution()
print(s.isIsomorphic("egg","add"))#true
print(s.isIsomorphic("foo","bar"))   #false
#print(s.isIsomorphic("paper","title"))  #true
print(s.isIsomorphic("bbaaba","aabbba"))  #false
#print(s.isIsomorphic("bbbaaaba","aaabbbba"))  #false