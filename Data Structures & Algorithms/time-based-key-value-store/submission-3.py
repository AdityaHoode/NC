from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if not self.time_map[key]:
            return ""
        else:
            saved_timestamps=list(self.time_map[key].keys())
            target=timestamp
            l,r=0,len(saved_timestamps)-1
            while l<=r:
                m=(l+r)//2
                if target>saved_timestamps[m]:
                    l=m+1
                elif target<saved_timestamps[m]:
                    r=m-1
                else:
                    return self.time_map[key][target]
            if r<0:
                return ""
            else: 
                return self.time_map[key][saved_timestamps[r]] 
            