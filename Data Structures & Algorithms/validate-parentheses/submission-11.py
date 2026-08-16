class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '{':'}',
            '(':')',
            '[':']'
        }
        brackets_rev={v:k for k,v in brackets.items()}
        stack = []
        #seen = set()
        '''if len(s)%2==1:
            return False
        for char in s:
            if char not in brackets:
                if not stack:
                    return False
                letter = stack.pop()
                while letter!=brackets_rev(char):
                    letter=stack.pop()
                if letter not in brackets_rev:
                    return False
                stack.append(char)
            else:
                stack.append(char)
        return True'''
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

            
            

         

            
            
            

        