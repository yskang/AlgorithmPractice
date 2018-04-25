import sys

if __name__ == '__main__':
    ps = sys.stdin.readline().strip()
    try:
        eval('0,' + ps.replace(')', '),').replace(']', '],'))
        ps = ps.replace("()", "(1)")
        ps = ps.replace("[]", "[1]")
        ps = ps.replace("(", "+2*(")
        ps = ps.replace("[", "+3*(")
        ps = ps.replace("]", ")")
        print(eval(ps))
    except:
        print(0)
        exit(0)