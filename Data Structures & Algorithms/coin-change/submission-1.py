class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [10000] * (amount + 2)
        ans[0] = 0
        for coin in coins:
            if coin > amount:
                break
            ans[coin] = 1
        for i in range(1, amount + 2):
            for coin in coins:
                idx = i - coin
                if idx <= 0:
                    continue
                else:
                    ans[i] = min(ans[i], ans[idx] + 1)

        return ans[amount] if ans[amount] != 10000 else -1