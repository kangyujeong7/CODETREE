N = input()
text = list(N)

text[1] = 'a'
text[-2] = 'a'

print("".join(text))