# Title: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/


from typing import List


class Problem:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(num_courses)]
        
        for a, b in prerequisites:
            if a == b:
                return False
            edges[a].append(b)


        for scc, _ in self.get_scc([i for i in range(num_courses)], edges):
            if len(scc) > 1:
                return False
        return True
        
    
    def get_scc(self, vertices, edges):
        identified = set()
        stack = []
        index = {}
        boundaries = []

        for v in vertices:
            if v not in index:
                to_do = [('VISIT', v)]
                while to_do:
                    operation_type, v = to_do.pop()
                    if operation_type == 'VISIT':
                        index[v] = len(stack)
                        stack.append(v)
                        boundaries.append(index[v])
                        to_do.append(('POSTVISIT', v))
                        to_do.extend(
                            reversed([('VISITEDGE', w) for w in edges[v]]))
                    elif operation_type == 'VISITEDGE':
                        if v not in index:
                            to_do.append(('VISIT', v))
                        elif v not in identified:
                            while index[v] < boundaries[-1]:
                                boundaries.pop()
                    else:
                        if boundaries[-1] == index[v]:
                            boundaries.pop()
                            scc = set(stack[index[v]:])
                            ordered_scc = stack[index[v]:]
                            del stack[index[v]:]
                            identified.update(scc)
                            yield scc, ordered_scc



def solution():
    num_courses = 2
    prerequisites = [[0, 1]]
    problem = Problem()
    return problem.can_finish(num_courses, prerequisites)


def main():
    print(solution())


if __name__ == '__main__':
    main()