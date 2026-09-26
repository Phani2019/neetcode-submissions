class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups:defaultdict=defaultdict(list)
        answer=[]
        for i in strs:
            sortedword=''.join(sorted(i))
            groups[sortedword].append(i)
        for j in groups.values():
            answer.append(j)
        return answer

        