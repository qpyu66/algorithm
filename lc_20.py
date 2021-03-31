class Solution:
    def isValid(self, s: str) -> bool:
#s="()[]"
s="([)]"
#s="(){()[{][]"
slist = list(s)
an =[]
print(slist)
  
for i in s:
    #print(i)
    if i == '[' or i == '{' or i == '(' :
        print('[i > ',i)
        an.append(i)
    #괄호 맞는 것 끼리 맨 뒤에서부터 pop      
    elif i == ']' or i == '}' or i == ')':
        an.pop()

print('an> ', an)

if len(an) != 0:
    print('false')
        return ""
        
    
    
s = Solution()
lists = "()"
s.isValid(lists)    