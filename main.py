from tokenizer import Tokenizer
from paser import Paser


def calculator(s):
    tokens = Tokenizer(s).tokens
    if len(tokens) > 1:
        p = Paser(tokens)
        print('结果为：', p.counter(p.n))
        return p.counter(p.n)
    else:
        print('结果为：', tokens[0][1])
        return tokens[0][1]


def main():
    while True:
        s = input("请输入算术表达式:")
        calculator(s)
        print('-------------')


def test():
    assert calculator('3*(2+4)') == 18
    assert calculator('(2+4)*3') == 18
    assert calculator('2-4*3') == -10
    assert calculator('6/2+1') == 4
    assert calculator('(10/(2*5))') == 1
    assert calculator('(5*((6+2)/2))') == 20


if __name__ == '__main__':
    test()
    # main()