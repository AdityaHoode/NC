# R1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num]=d.setdefault(num,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in d.items():
            buckets[freq].append(num)
        print(buckets)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            if buckets[i]==[]:
                continue
            res.extend(buckets[i])
            if len(res)==k:
                return res