class Solution:

    def encode(self, strs: List[str]) -> str:
        op = ""
        for i in range(len(strs)):
            op+=str(len(strs[i]))+"#"+strs[i]
        return op
    def decode(self, s: str) -> List[str]:
        op=[]
        i=0
        j=0
        while i<len(s):
            while s[j]!='#':
               j+=1
            length=int(s[i:j])
            i=j+1
            word = s[i:i+length]
            op.append(word)
            i+=length
            j=i
        return op