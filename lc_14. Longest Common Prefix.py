from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lslen = len(strs)
        print(lslen, strs, type(strs))
        sortedwords = sorted(strs, key=len)
        sortlen = len(sortedwords[0])
        print('s> ',sortedwords,', ',sortlen)
        non = ""
        if not strs:
            return non
        
        oc =[]
        for i in range(sortlen):
            a = strs[0][i]
            #print('i >',i,' ,a > ',a)
            for j in range(1,lslen):
                b = sortedwords[j][i]
                #print(sortedwords[j][i], 'j >', j)            
                if strs[0][i] != sortedwords[j][i]:
                    #oc.append(non)
                    return ""
                    #break
            print('a > ',a)        
            oc.append(a)   
            print('oc > ', oc)
            ocjoin = ''.join(oc)    
        print('ocjoin >',ocjoin)
        
        return ocjoin
            

s = Solution()
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
s.longestCommonPrefix(strs)