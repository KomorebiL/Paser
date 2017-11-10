class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Paser:
    def __init__(self, tokens):
        self.result = []
        self.i = 0
        self.tokens = tokens
        self.paser_m(' ')
        self.n = Node()
        self.maketree(self.result, self.n)

    def apnd(self, n):
        return self.result.append(n)

    def paser_m(self, n):
        sign = self.tokens[self.i][1]
        if sign == '+' or sign == '-':
            self.i += 1
            n += ' '
            self.apnd((self.tokens[self.i], len(n)))
            self.paser_e(n)
        else:
            self.paser_e(n)
            if self.i < len(self.tokens) - 1:
                print('错误', self.tokens[self.i - 1][1], self.i)
                exit(0)

    def paser_e(self, n):
        self.paser_t(n)
        self.paser_e1(n)

    def paser_e1(self, n):
        if self.i >= len(self.tokens):
            return
        else:
            sign = self.tokens[self.i][1]
            if sign == '+' or sign == '-':
                n += ' '
                self.apnd((self.tokens[self.i], len(n)))
                self.i += 1
                self.paser_t(n)
                self.paser_e1(n)

    def paser_t(self, n):
        self.paser_f(n)
        self.paser_t1(n)

    def paser_t1(self, n):
        if self.i >= len(self.tokens):
            return
        else:
            sign = self.tokens[self.i][1]
            if sign == '*' or sign == '/':
                n += ' '
                self.apnd((self.tokens[self.i], len(n)))
                self.i += 1
                self.paser_f(n)
                self.paser_t1(n)

    def paser_f(self, n):
        t = self.tokens[self.i]
        if t[0] == 'NUMBER':
            n += ' '
            self.apnd((t, len(n)))
            self.i += 1
        elif t[1] == '(':
            n += ' '
            self.i += 1
            self.paser_e(n)
            t = self.tokens[self.i]
            if t[1] == ')':
                n += ' '
                self.i += 1
            else:
                print("缺少)", t, self.i)
                exit(0)
        else:
            print("文法错误", self.tokens[self.i][1], self.i)
            exit(0)

    @staticmethod
    def get_number(result):
        m = ''
        for s in result:
            if s[0][1] in '+-*/':
                m = s
                print(s)
                break
        return m

    def min_sign(self, result):
        m = self.get_number(result)
        index = False
        for i, l in enumerate(result):
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
        else:
            i = self.min_sign(result)
            if i is not False:
                n.data = result[i][0]
                n.left = Node()
                n.right = Node()
                self.maketree(result[0: i], n.left)
                self.maketree(result[i + 1:], n.right)

    def counter(self, tree):
        if tree is not None:
            sign = tree.data[0]
            if sign is 'NUMBER':
                return int(tree.data[1])
            elif sign is 'ADD':
                return self.counter(tree.left) + self.counter(tree.right)
            elif sign is 'SUB':
                return self.counter(tree.left) - self.counter(tree.right)
            elif sign is 'MUL':
                return self.counter(tree.left) * self.counter(tree.right)
            else:
                return self.counter(tree.left) / self.counter(tree.right)
