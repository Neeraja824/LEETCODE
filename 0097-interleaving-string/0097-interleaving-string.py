class Solution:
    def isInterleave(self, s1, s2, s3):

        @lru_cache(None)
        def function(i,j,k,s1,s2,s3):
            if i == len(s1) and j == len(s2):
                return True if k == len(s3) else False 

            if k == len(s3):
                return False 

            if i < len(s1) and s1[i] == s3[k]:
                if function(i+1,j,k+1,s1,s2,s3):
                    return True 

            if j < len(s2) and s2[j] == s3[k]:
                if function(i,j+1,k+1,s1,s2,s3):
                    return True 

            return False 

        return function(0,0,0,s1,s2,s3)