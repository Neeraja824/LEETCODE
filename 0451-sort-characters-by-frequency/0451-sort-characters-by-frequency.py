from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        ans=""
        for ch,count in freq.most_common():
            ans+=ch*count
        return ans