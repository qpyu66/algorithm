class Solution:
    def isValid(self, s: str) -> bool:
        slist = list(s)
        slen = len(slist)       
        an =[]        

        if len(s) % 2 !=0:
            return False
        if len(s) == 0:
            return False
        
        for i in range(0,slen):
            if slist[i] in ['(','{','['] :
                an.append(slist[i])
            else:
                if slist[i] == ')' and an.pop() !='(' :   
                    return False
                elif slist[i] == '}' and an.pop() !='{' :   
                    return False
                elif slist[i] == ']' and an.pop() !='[' :   
                    return False
        return True
    
s = Solution()
lists = "()[]"
s.isValid(lists)    