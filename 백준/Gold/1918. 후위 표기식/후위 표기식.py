import sys

s = list(map(str, sys.stdin.readline().strip()))
stack = []
result = ""

for i in s:
    if i.isalpha():
        result += i
    
    elif i == '(':
        stack.append(i)
        
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1]=='/'):
            result += stack.pop()
        stack.append(i)
        
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(i)
        
    elif i == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()

while stack:
    result += stack.pop()
    
print(result)