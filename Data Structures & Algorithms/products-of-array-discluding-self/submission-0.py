class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        lp=1
        rp=1
        for i in range(1,len(nums)):
            lp*=nums[i-1]
            left.append(lp)

        for i in range(len(nums)-2,-1,-1):
            rp*=nums[i+1]
            right.append(rp)
        right.reverse()

        op=[]
        for l,r in zip(left,right):
            op.append(l*r)

        return op