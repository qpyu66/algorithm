class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = ["flower","flow","flight"]
        lslen = len(str)
        sortedwords = sorted(str, key=len)
        sortlen = len(sortedwords[0])

        oc = []
        for s in range(lslen):
            os = list(str[s])
            oc.append(os)

        oclen = len(oc)
        alloc = []
        for i in range(len(oc)):
            for j in range(sortlen):
                if (oc[i][j] == oc[i + 1][j] == oc[i + 2][j]):
                    print('ok', oc[i][j], oc[i + 1][j], oc[i + 2][j])
                    alloc.append(oc[i][j])
            alloc.append("")

        return ''.join(alloc)

        # ans = ''.join(alloc)
        #
        #
        # return ans



