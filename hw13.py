import sys
stack = []
while True:
    data = sys.stdin.readline().rstrip('\n')
    if data == "quit":
        break
    stack.append(data)
while stack:
    print(stack.pop())