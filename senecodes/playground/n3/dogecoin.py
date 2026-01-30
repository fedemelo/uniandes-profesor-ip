def solution(prices) -> int:
    profit = 0
    for i in range(1, len(prices)):
        tran = prices[i]-prices[i-1]
        if tran > 0:
            profit += tran
    return profit

print(solution([1,7,3,4,5])) # 7