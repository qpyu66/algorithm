class Solution:
    def reverse(self, x: int) -> int:
       
        a = list(str(x))
        if x <0:
            b = a[1:]
            c = b[::-1]
            r = ''.join(c)
            ans = int(r)*-1
            if ans <  2**31*-1:
                return 0
            else:
                return ans
        else:
            b = a[::-1]
            ans = int(''.join(b))
            if ans > 2**31:
                return 0
            else:
                return ans



s = Solution()
#print(s.reverse(123))
print(s.reverse(-123))        
print(s.reverse(120))