class Solution:
    def binary_search(self, nums: List[tuple[int]], target: int, deflection_index: int):
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target>nums[m][1]:
                l=m+1
            elif target<nums[m][1]:
                r=m-1
            else:
                return nums[m][0]
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        deflection_index=r
        snums=[(i,val) for i,val in enumerate(nums)]
        res1=self.binary_search(snums[:r], target, deflection_index)
        res2=self.binary_search(snums[r:], target, deflection_index)
        return res2 if res1==-1 else res1
