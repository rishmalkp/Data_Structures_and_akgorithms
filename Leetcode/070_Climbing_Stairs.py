'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0,1]
        
        for i in range(2,n+2):
            dp.append(dp[i-2]+dp[i-1])
        return dp[n+1]