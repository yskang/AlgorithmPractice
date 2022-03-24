import sys
from collections import defaultdict
from typing import DefaultDict, List
 
 
read_single_int = lambda: int(sys.stdin.readline().strip())
read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
 
  
def solution(n: int, m: int, child_of: DefaultDict, odds: List, values: DefaultDict):
    value = ['0' for _ in range(m)]
 
    current = n+1
 
    while odds:
        x = odds.pop()
        y = odds.pop()
        child_of[x].add(current)
        child_of[y].add(current)
        child_of[current].add(x)
        child_of[current].add(y)
        # current += 1
 
    while True:
        ans = []
        st = []
        start = None
 
        for node in child_of:
            if child_of[node]:
                start = node
                break
        else:
            break
 
        st.append(start)
        while st:
            v = st[-1]
            if not child_of[v]:
                ans.append(v)
                st.pop()
            else:
                to = child_of[v].pop()
                child_of[to].discard(v)
                st.append(to)
 
        for i in range(len(ans)-1):
            v = (ans[i], ans[i+1]) 
            if v in values:
                value[values[v]] = '1'
 
    return ''.join(value)
 
 
 
def main():
    t = read_single_int()
    for _ in range(t):
        child_of = defaultdict(lambda: set())
        n, m = read_list_int()
        values = defaultdict(lambda: 0)
        for i in range(m):
            x, y = read_list_int()
            child_of[x].add(y)
            child_of[y].add(x)
            values[(x, y)] = i
        odd = []
        for i in range(1, n+1):
            if len(child_of[i]) % 2:
                odd.append(i)
        print(solution(n, m, child_of, odd, values))
 
 
if __name__ == '__main__':
    main()