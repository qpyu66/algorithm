from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lslen = len(strs)
        print(lslen, strs, type(strs))
        sw = sorted(strs, key=len)
        swlen = len(sw[0])
        print('s> ', sw, ', ', swlen)

        oc = []
        for i in range(swlen):
            a = sw[0][i]
            # print('i >',i,' ,a > ',a)
            for j in range(1, lslen):
                b = sw[j][i]
                if sw[0][i] != sw[j][i]:
                    print('i> ', i)
                    return sw[0][:i]


s = Solution()
strs = ["flower", "flow", "flight"]
# strs = ["dog","racecar","car"]
s.longestCommonPrefix(strs)