class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = list(str(x))
        # print(a)
        # b = a[::-1]
        # print(b )
        # print( ''.join(b))
        if x <0: #음수처리
            #b[0] = a[0]
            b = a[::-1]
            print(b)
            
        else:
            b = a[::-1]
        return ''.join(b)
        

        


s = Solution()
#print(s.reverse(123))
print(s.reverse(-123))        