import bisect


class Solution:
    def getSkyline(self, buildings):
        skyline = []
        edges = []
        current_height = 0
        behind_heights = []

        for building in buildings:
            edges.append((building[0], building[2], "left"))
            edges.append((building[1], building[2], "right"))

        edges = sorted(edges, key=lambda edge: edge[0])

        for edge in edges:
            if edge[2] == "left":
                if edge[1] > current_height:
                    i = bisect.bisect_left(behind_heights, current_height)
                    behind_heights = behind_heights[:i] + [current_height] + behind_heights[i:]
                    current_height = edge[1]
                    if skyline and skyline[-1][0] == edge[0]:
                        if current_height > skyline[-1][1]:
                            skyline.pop()
                            skyline.append([edge[0], current_height])
                    else:
                        skyline.append([edge[0], current_height])

                else:
                    i = bisect.bisect_left(behind_heights, edge[1])
                    behind_heights = behind_heights[:i] + [edge[1]] + behind_heights[i:]
            else:
                if edge[1] == current_height:
                    current_height = behind_heights.pop()
                    skyline.append([edge[0], current_height])
                else:
                    behind_heights.remove(edge[1])

            if len(skyline) > 1 and skyline[-1][1] == skyline[-2][1]:
                skyline.pop()
            if len(skyline) > 1 and skyline[-1][0] == skyline[-2][0]:
                a, b = skyline.pop(), skyline.pop()
                skyline.append([a[0], min(a[1], b[1])])


        return skyline


if __name__ == '__main__':
    sol = Solution()
    print(sol.getSkyline([[0, 3, 3], [1, 5, 3], [2, 4, 3], [3, 7, 3]]))
    print(sol.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]))
    print(sol.getSkyline([[0, 2, 3], [2, 5, 3]]))
    print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
