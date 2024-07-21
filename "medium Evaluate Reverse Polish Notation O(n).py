def evalRPN(self, tokens: List[str]) -> int:
    num = []

    for token in tokens:
        if token == '+':
            num.append(num.pop() + num.pop())
        elif token == '-':
            num.append(- num.pop() + num.pop())
        elif token == '*':
            num.append(num.pop() * num.pop())
        elif token == '/':
            div = num.pop()
            num.append(int(num.pop() / div))
        else:
            num.append(int(token))

    return num[0]
