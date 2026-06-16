class Solution:
    def findDeflectionIndex(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return r
    
    def binary_search(self, nums: List[int], target: int, l: int, r: int) -> int:
        while l<=r:
            m=(l+r)//2
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if nums[0]<=nums[-1]:
            return self.binary_search(nums, target, 0, len(nums)-1)
        deflection_index=self.findDeflectionIndex(nums)
        if target>=nums[deflection_index] and target<=nums[-1]:
            return self.binary_search(nums, target, deflection_index, len(nums)-1)
        else:
            return self.binary_search(nums, target, 0, deflection_index-1)
