class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        print(s)
        length=len(s)
        for i in range(length):
            if s[i]==s[-i-1]:
                continue
            else:
                return False
        return True 