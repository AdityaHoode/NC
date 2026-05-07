import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=re.sub(r'\s+|[^a-zA-Z0-9]','',s)
        return s1.lower()==s1[::-1].lower()