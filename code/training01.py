def calculation(expression):
    stack = []
    for i in expression.split(' '):
        # 現在のスタック内容
        print(stack)
        if i == '+':
            # ＋の場合、スタックから2つ取り出して加算、再度格納
            b, a = stack.pop(),  stack.pop()
            stack.append(a + b)
        elif i == '-':
            # -の場合、スタックから2つ取り出して減算、再度格納
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif i == '*':
            # *の場合、スタックから2つ取り出して減算、再度格納
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == '/':
            # /の場合、スタックから2つ取り出して減算、再度格納
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        else:
            # 演算子以外（数字）の場合、その値を格納
            stack.append(int(i))
    return stack[0]

print(calculation('3 5 2 - * 4 1 + 5 * +'))