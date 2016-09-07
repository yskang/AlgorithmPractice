text = input()
if text == '':
    print(0)
elif len(text) == text.count(' '):
    print(len(text)-1)
else:
    print(text.strip().count(' ') + 1)
