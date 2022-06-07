from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lslen = len(strs)
        sortedwords = sorted(strs, key=len)
        non = ""
        if not str:
            return non
        sortlen = len(sortedwords[0])

        for i in range(sortlen):
            for j in range(1, lslen):
                if sortedwords[0][i] != sortedwords[j][i]:
                    return sortedwords[0][:i]


s = Solution()
# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
 #빈 리스트가 들어가면 0 인덱스에 해당하는 element가 없어서 sortlen에서 에러남
strs = [""]
s.longestCommonPrefix(strs)


