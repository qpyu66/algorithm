"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        non = ""
        #빈 리스트 체크
        if not strs:
            return non
        
        #제일 작은 문자열
        mstrs = min(strs, key=len)
        slen = len(mstrs)
        #print("strs min> ", mstrs)
       
        #입력받은 리스트len 만큼
        for i in range(slen):
            a = strs[0][i]
            #strs[0]와 비교를 위해 strs[i] i가 1 부터 증가하면서 비교 
            for j in range(1, len(strs)):
                if strs[j][i] != a: #문자 동일하지 않으면 빈값 입력
                    return non
            non = non + a #문자 더하기
            
        return non
        

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix([""]))
print(s.longestCommonPrefix(["ab","a"]))
