class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA, lenB=len(nums1), len(nums2)
        if lenB<lenA:
            return self.findMedianSortedArrays(nums2,nums1)
        
        num_left_elements=(lenA+lenB+1)//2
        total_elements=lenA+lenB

        l,r=0,lenA
        while l<=r:
            mA=(l+r)//2
            mB=num_left_elements-mA

            aR=float('-inf') if mA==0 else nums1[mA-1]
            bR=float('-inf') if mB==0 else nums2[mB-1]
            aL=float('+inf') if mA==lenA else nums1[mA]
            bL=float('+inf') if mB==lenB else nums2[mB]

            if bR>aL:
                l=mA+1
            elif aR>bL:
                r=mA-1
            else:
                if total_elements%2==0:
                    return (max(aR,bR)+min(aL,bL))/2
                else:
                    return max(aR,bR)

        return 0 