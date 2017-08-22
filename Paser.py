class Token:
    def __init__(self, s):
        self.number = '0123456789'
        self.sign = '+-*/'
        self.lr = '()'
        self.tokens = []
        self.getToken(s)

    def getToken(self, texts):
        index = 0
        length = len(texts)
        flag = 0
        String = ''
        apend = self.tokens.append
        while index < length:
            text = texts[index]
            if flag == 0:
                if text in self.number:
                    flag = 1
                elif text in self.sign:
                    flag = 2
                elif text == "(":
                    flag = 3
                elif text == ')':
                    flag = 4
                else:
                    print(("第{0}列出现了异常字符{1}".format(index + 1, text)))
                    exit(0)

            elif flag == 1:
                if text not in self.number:
                    flag = 0
                    apend(('NUMBER', String))
                    String = ""
                else:
                    String = String + text
                    index += 1
                    if index >= length:
                        apend(('NUMBER', String))

            elif flag == 2:
                if text == '+':
                    apend(("ADD", "+"))
                elif text == '-':
                    apend(('SUB', '-'))
                elif text == '*':
                    apend(('MUL', '*'))
                else:
                    apend(('DIV', '/'))
                flag = 0
                index += 1

            elif flag == 3:
                apend(('LEFT', '('))
                flag = 0
                index += 1

            elif flag == 4:
                apend(('RIGHT', ')'))
                flag = 0
                index += 1
        return self.tokens

class Paser():
    def __init__(self, tokens):
        self.result = []
        self.i = 0
        self.tokens = tokens
        self.paser_M(' ')
        self.n = Node()
        self.maketree(self.result, self.n)


    def apnd(self, n):
        return self.result.append(n)

    def paser_M(self, n):
        sign = self.tokens[self.i][1]
        if sign == '+' or sign == '-':
            self.i += 1
            n += ' '
            self.apnd((self.tokens[self.i], len(n)))
            self.paser_E(n)
            return
        else:
            self.paser_E(n)
            if self.i < len(self.tokens) - 1:
                print('错误', self.tokens[self.i - 1][1], self.i)
                exit(0)
            return

    def paser_E(self, n):
        self.paser_T(n)
        self.paser_E1(n)
        return

    def paser_E1(self, n):
        if self.i >= len(self.tokens):
            return
        else:
            sign = self.tokens[self.i][1]
            if sign == '+' or sign == '-':
                n += ' '
                self.apnd((self.tokens[self.i], len(n)))
                self.i += 1
                self.paser_T(n)
                self.paser_E1(n)
            return

    def paser_T(self, n):
        self.paser_F(n)
        self.paser_T1(n)
        return

    def paser_T1(self, n):
        if self.i >= len(self.tokens):
            return
        else:
            sign = self.tokens[self.i][1]
            if sign == '*' or sign == '/':
                n += ' '
                self.apnd((self.tokens[self.i], len(n)))
                self.i += 1
                self.paser_F(n)
                self.paser_T1(n)
            return

    def paser_F(self, n):
        t = self.tokens[self.i]
        if t[0] == 'NUMBER':
            n += ' '
            self.apnd((t, len(n)))
            self.i += 1
            return
        elif t[1] == '(':
            n += ' '
            self.i += 1
            self.paser_E(n)
            t = self.tokens[self.i]
            if t[1] == ')':
                n += ' '
                self.i += 1
                return
            else:
                print("缺少)", t, self.i)
                exit(0)
        else:
            print("文法错误", self.tokens[self.i][1], self.i)
            exit(0)

    def minsign(self, result):
        for i in range(len(result)):
            if result[i][0][1] in '+-*/':
                m = result[i]
                break
        index = False
        for i in range(len(result)):
            l = result[i]
            s = l[0][1]
            n = l[1]
            if s in '+-*/':
                if n <= m[1]:
                    m = l
                    index = i
        return index

    def maketree(self, result, n):
        if len(result) == 1:
            n.data = result[0][0]
            return
        else:
            i = self.minsign(result)
            if i != False:
                n.data = result[i][0]
                n.left = Node()
                n.right = Node()
                self.maketree(result[0 : i], n.left)
                self.maketree(result[i + 1:], n.right)

    def counter(self, tree):
        if tree != None:
            sign = tree.data[0]
            if sign == 'NUMBER':
                return int(tree.data[1])
            elif sign == 'ADD':
                return self.counter(tree.left) + self.counter(tree.right)
            elif sign == 'SUB':
                return self.counter(tree.left) - self.counter(tree.right)
            elif sign == 'MUL':
                return self.counter(tree.left) * self.counter(tree.right)
            else:
                return self.counter(tree.left) / self.counter(tree.right)

class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def main():
    while True:
        S = input("请输入算术表达式:")
        tokens = Token((S)).tokens
        if len(tokens) > 1:
            p = Paser(tokens)
            print('结果为：', p.counter(p.n))
        else:
            print('结果为：', tokens[0][1])
        print('-------------')

main()
