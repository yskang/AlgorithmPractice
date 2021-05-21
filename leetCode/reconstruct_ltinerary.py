# Title: Reconstruct Ltinerary
# Link: https://leetcode.com/problems/reconstruct-itinerary/


from typing import List
from collections import defaultdict

class Problem:
    def find_itinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(lambda: [])
        tickets = sorted(tickets, reverse=True)
        for start, end in tickets:
            g[start].append(end)

        ans = []
        stack = ['JFK']

        while stack:
            v = stack[-1]
            if len(g[v]) == 0:
                ans.append(v)
                stack.pop()
            else:
                to = g[v].pop()
                stack.append(to)
        
        return ans[::-1]
    



def solution():
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    problem = Problem()
    return problem.find_itinerary(tickets)


def main():
    print(solution())


if __name__ == '__main__':
    main()