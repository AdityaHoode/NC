class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_a,len_b=len(nums1),len(nums2)
        if len_b<len_a:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left,right=0,len_a
        left_elements=(len_a+len_b+1)//2
        total_elements=len_a+len_b
        
        while left<=right:
            mid_a=(left+right)//2
            mid_b=left_elements-mid_a

            a_right = float('-inf') if mid_a==0 else nums1[mid_a-1]
            b_right = float('-inf') if mid_b==0 else nums2[mid_b-1]
            a_left = float('inf') if mid_a==len_a else nums1[mid_a]
            b_left = float('inf') if mid_b==len_b else nums2[mid_b]

            if b_right > a_left:
                left=mid_a+1
            elif a_right>b_left:
                right=mid_a-1
            else:
                if total_elements%2==0:
                    return (max(a_right,b_right)+min(a_left,b_left))/2
                else:
                    return max(a_right,b_right)
            
        return 0
            