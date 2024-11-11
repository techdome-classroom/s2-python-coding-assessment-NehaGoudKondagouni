class Solution(object):
    def isValid(self, s):
        stack = []
    
        dict1 = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in dict1:
                top = stack.pop() if stack else '#'
                
                if dict1[char] != top:
                    return False
            else:
                stack.append(char)
        
        return not stack





