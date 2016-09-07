inputWord = 'baekjoon'.strip()
alphabets = map(chr, range(97, 123))
print(' '.join(list(map(lambda c: str(inputWord.find(c)), alphabets))))