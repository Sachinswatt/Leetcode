class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for i in range(len(accounts)):
            current = 0
            for j in range(len(accounts[i])):
                current+=accounts[i][j]
                if current>max_wealth:
                    max_wealth = current

                
                

        return max_wealth
        