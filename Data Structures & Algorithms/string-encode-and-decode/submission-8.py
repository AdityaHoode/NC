class Solution:

    def encode(self, strs: List[str]) -> str:
        op=""
        for word in strs:
            length=len(word)
            op+=f"{length}#{word}"
        return op
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        op=[]
        length=""
        i=0
        while i<len(s):
            if s[i]!="#":
                length+=s[i]
                i+=1
                continue
            length=int(length)
            op.append(s[i+1:i+length+1])
            i+=length+1
            length=""
        return op