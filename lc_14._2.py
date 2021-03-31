from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = ["flower", "flow", "flight"]
        lslen = len(strs)
        sortedwords = sorted(strs, key=len)
        sortlen = len(sortedwords[0])

        oc = []
        for s in range(lslen):
            os = list(strs[s])
            oc.append(os)

        alloc = []
        for j in range(sortlen):
            if (oc[0][j] == oc[1][j] == oc[2][j]):
                alloc.append(oc[0][j])
            else:
                alloc.append("")

        #alloc.append("")
        return ''.join(alloc)


