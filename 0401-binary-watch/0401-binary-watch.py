class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn>8: return []
        ans=[]
        for hour in range(12):
            for minu in range(60):
                if hour.bit_count()+minu.bit_count()==turnedOn:
                    ans.append(f"{hour}:{minu:02d}")
        return ans