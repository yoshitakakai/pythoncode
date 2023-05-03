<<<<<<< HEAD
import numpy
import math

def make_rotate_matrix(red):
    return numpy.array([[math.cos(red), -math.sin(red)],
                        [math.sin(red), math.cos(red)]]).transpose()


def main():

    num = 20
    base = numpy.array([1, 0])
    print('degree \t resualt')

    for x in range(num + 1):
        rad = x * math.pi * 2 / num
        rot = make_rotate_matrix(rad)
        deg = 360 / num * x
        result = base @ rot
        print(deg, '\t', result)

if __name__ == '__main__':
    main()
=======
<<<<<<< HEAD
colors = ["blue", "green", "yellow"]
print(colors)
item = colors.pop()

print(item)
print(colors)
=======
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
>>>>>>> origin/main
>>>>>>> refs/remotes/origin/main
