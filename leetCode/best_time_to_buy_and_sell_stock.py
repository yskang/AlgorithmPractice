# Title: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def max_profit(self, prices: list) -> int:
        buy = 10**10
        max_profit = 0
        prev_price = 0
        for price in prices:
            if price < buy:
                buy = price
            elif prev_price < price:
                max_profit = max(max_profit, price-buy)
            prev_price = price
        return max_profit


def problem():
    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()
    return solution.max_profit(prices)


def main():
    print(problem())


if __name__ == '__main__':
    main()