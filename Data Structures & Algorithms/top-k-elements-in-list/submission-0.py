class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        arr=[]
        for num,cnt in counts.items():
            arr.append([cnt,num])
        arr.sort()
        rs=[]
        while len(rs)<k:
            rs.append(arr.pop()[1])
        return rs
        
        
        