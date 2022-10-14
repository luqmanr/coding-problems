class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        customer_wealths = []
        for i,customer in enumerate(accounts):
            customer_wealth = 0
            for j,money in enumerate(customer):
                customer_wealth += money
            customer_wealths.append(customer_wealth)
        
        return max(customer_wealths)