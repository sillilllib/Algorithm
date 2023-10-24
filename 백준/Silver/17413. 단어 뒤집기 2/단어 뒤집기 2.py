import sys

s = list(map(str, sys.stdin.readline().strip()))

result = ""
word = ""
reverse = True

for c in s:

    if c == '<':
        reverse = False
        result += word
        word = c

    elif c == '>':
        reverse = True
        result += (word + '>')
        word = ""

    elif c == ' ':
        result += word + c
        word = ""

    elif reverse:
        word = c + word

    else:
        word += c

result += word
print(result)