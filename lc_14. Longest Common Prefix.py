from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lslen = len(strs)
        sortedwords = sorted(strs, key=len)
        sortlen = len(sortedwords[0])
        print(sortedwords, type(sortedwords), sortlen)

        oc = []
        for s in range(lslen):
            os = list(sortedwords[s])
            oc.append(os)

        oclen = len(oc)
        alloc = []

        for j in range(sortlen):
            if (oc[0][j] == oc[1][j] == oc[2][j]):
                print('ok', oc[0][j], oc[1][j], oc[2][j])
                alloc.append(oc[0][j])
                print(j)

        alloc.append("")

        return ''.join(alloc)


s = Solution()
# strs = ['flower', 'flow', 'flight']
strs = ['flower', 'flowes', 'floweds']
s.longestCommonPrefix(strs)