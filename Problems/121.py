# Kamesh Vedula
# Problem: Best Time to Buy and Sell Stock

def maxProfit(self, prices):
    if not prices or len(prices) is 1:
        return 0
    
    low, maxDiff = prices[0], 0
    
    for i in range(1, len(prices)):
        if prices[i] < low:
            low = prices[i]
        else:
            diff = prices[i] - low
            
            if diff > maxDiff:
                maxDiff = diff
    
    return maxDiff