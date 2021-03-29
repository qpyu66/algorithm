class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        lenx = len(strx)
        midlen = int(lenx/2)
        if x <0 : return False
    
        for i in range(0,midlen+1):
            ax = x // (10**i)
            bx = ax % 10
            print('ax, ',ax,'bx, ',bx,'x ',strx[i])
            if int(strx[i]) == bx:
                continue
            if int(strx[i]) != bx:
                return False
            
        return True     
      
            
s = Solution()
s.isPalindrome(1241)