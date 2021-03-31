from typing import List
from collections import OrderedDict


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lslen = len(strs)
        sortedwords = sorted(strs, key=len)
        sortlen = len(sortedwords[0])

        oc = []
        for i in range(sortlen):
            a = sortedwords[0][i]
            for j in range(1, lslen):
                b = sortedwords[j][i]
                if a != b:
                    oc.pop()
                    break

                oc.append(a)
        ans = ''.join(OrderedDict.fromkeys(oc))
        return ans

s = Solution()
strs = ["flower","flow","flight"]
s.longestCommonPrefix(strs)