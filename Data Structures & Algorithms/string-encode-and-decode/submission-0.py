class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result = result + str(len(i)) + '#' + i
        return result

    def decode(self, s: str) -> List[str]:
        str_arr=[]
        i = 0
        while i < len(s):
            j=i
            while s[j]!='#':
                j=j+1
            length=int(s[i:j])
            i=j+1
            str_arr.append(s[i:i+length])
            i+=length
        return str_arr



