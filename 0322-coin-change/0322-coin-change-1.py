class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
    
        df = [amount + 1] * (amount + 1)
        df[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    df[a] = min(df[a], 1 + df[a - c])
        
        return df[amount] if df[amount] != amount + 1 else -1