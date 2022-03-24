# https://www.acmicpc.net/problem/2941


def count_Croatian(line):
    croatian_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for word in croatian_words:
        line = line.replace(word, "+")
    return len(line)

if __name__ == "__main__":
    print(count_Croatian(input()))
