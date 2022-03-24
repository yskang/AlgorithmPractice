import sys

if __name__ == '__main__':
    ps = sys.stdin.readline().strip()
    stack = []
    try:
        for p in ps:
            if p == '(':
                stack.append(p)
            elif p == '[':
                stack.append(p)
            elif p == ')':
                if not stack:
                    break
                q = stack.pop()
                if q == '(':
                    stack.append(2)
                elif q in {')', '['}:
                    stack = []
                    break
                else:
                    v = q
                    while True:
                        if stack[-1] == '(':
                            stack.pop()
                            break
                        v += int(stack.pop())
                    stack.append(v * 2)
            elif p == ']':
                if not stack:
                    break
                q = stack.pop()
                if q == '[':
                    stack.append(3)
                elif q in {']', '('}:
                    stack = []
                    break
                else:
                    v = q
                    while True:
                        if stack[-1] == '[':
                            stack.pop()
                            break
                        v += int(stack.pop())
                    stack.append(v * 3)
            else:
                stack = []
                break

        print(sum(stack))
    except:
        print(0)