class Tokenizer:
    def __init__(self, s):
        self.number = '0123456789'
        self.sign = '+-*/'
        self.lr = '()'
        self.tokens = []
        self.get_token(s)

    def get_token(self, texts):
        index = 0
        length = len(texts)
        flag = 0
        string = ''
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
                    apend(('NUMBER', string))
                    string = ""
                else:
                    string += text
                    index += 1
                    if index >= length:
                        apend(('NUMBER', string))

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