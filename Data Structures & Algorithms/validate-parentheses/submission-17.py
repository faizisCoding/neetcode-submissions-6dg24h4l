class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{':'}',
            '(':')',
            '[':']'
        }
        brackets_rev={v:k for k,v in brackets.items()}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1]!=brackets_rev[char] and stack[-1] in brackets:
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False

            
            

         

            
            
            

        