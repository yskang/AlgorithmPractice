# https://www.acmicpc.net/problem/2941


def count_Croatian(line):
    croatian_dic = {"c=": True, "c-": True, "dz=": True, "d-": True, "lj": True, "nj": True, "s=": True, "z=": True}
    count = len(line)

    for i in range(len(line)-1):
        if line[i:i+2] in croatian_dic and croatian_dic[line[i:i+2]]:
            count -= 1
        if i+3 <= len(line) and line[i:i+3] in croatian_dic and croatian_dic[line[i:i+3]]:
            count -= 1

    return count


if __name__ == "__main__":
    print(count_Croatian(input()))
