class Solution:
    def removeInvalidParentheses(self, s):
        results = set()
        remove_index = -1
        ss = s
        w = True
        if s == "":
            return [""]
        while w:
            p = 0
            l = ss.count("(")
            r = ss.count(")")
            big = 0

            if l > r:
                big == 0
            else:
                big == 1

            for i in range(len(ss)):
                if ss[i] == "(":
                    p += 1
                    l -= 1
                elif ss[i] == ")":
                    p -= 1
                    r -= 1
                if p < 0:
                    remove_index = i
                    w = True
                    break
                else:
                    if big == 0:
                        if r < p:
                            remove_index = i
                            w = True
                            break

                if i == len(ss)-1:
                    w = False

            if w == False:
                results.add(ss)
            else:
                if remove_index == len(ss)-1:
                    if len(ss[:len(ss)-1]) > 0:
                        results.add(ss[:len(ss)-1])
                    break
                ss = ss[:remove_index]+ss[remove_index+1:]

        w = True
        ss = s
        
        while w:
            l = ss.count("(")
            r = ss.count(")")

            p = 0
            for i in range(len(ss)-1, -1, -1):
                if ss[i] == ")":
                    p += 1
                    r -= 1
                elif ss[i] == "(":
                    p -= 1
                    l -= 1
                if p < 0:
                    remove_index = i
                    w = True
                    break
                else:
                    if big == 0:
                        if l < p:
                            remove_index = i
                            w = True
                            break
                if i == 0:
                    w = False
            
            if w == False:
                results.add(ss)
            else:
                if remove_index == 0:
                    if len(ss[1:]) > 0:
                        results.add(ss[1:])
                    break
                ss = ss[:remove_index]+ss[remove_index+1:]

        if len(results) == 0:
            return [""]
        return list(results)
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeInvalidParentheses("()())()"))
    print(sol.removeInvalidParentheses("(a)())()"))
    print(sol.removeInvalidParentheses(")("))