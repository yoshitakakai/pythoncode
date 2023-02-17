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