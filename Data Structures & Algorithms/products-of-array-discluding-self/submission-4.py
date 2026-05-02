# R1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left=[1]
        # right=[1]
        # p=1
        # for i in range(len(nums)-1):
        #     p*=nums[i]
        #     left.append(p)
        # p=1
        # for i in range(len(nums)-1,0,-1):
        #     p*=nums[i]
        #     right.append(p)
        # op=[]
        # for l,r in zip(left,reversed(right)):
        #     op.append(l*r)
        # return(op)

        product=[1]
        prefix=1
        for i in range(len(nums)-1):
            prefix*=nums[i]
            product.append(prefix)
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            product[i]*=suffix
            suffix*=nums[i]
        
        return product