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
    
    def binary_search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
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
        deflection_index=self.findDeflectionIndex(nums)
        if target>=nums[deflection_index] and target<=nums[-1]:
            index=self.binary_search(nums[deflection_index:], target)
            return deflection_index+index if index!=-1 else index
        else:
            return self.binary_search(nums[:deflection_index], target)
