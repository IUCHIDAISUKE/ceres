# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis


INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token(object):
    def __init__(self, type, value: int):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self) -> str:
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return f'Token({self.type}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text) -> None:
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        while text[self.pos] == ' ':
            self.pos += 1

        num = 0
        while text[self.pos].isdigit():
            num *= 10
            num += int(text[self.pos])
            self.pos += 1
            if self.pos > len(text)-1 or not text[self.pos].isdigit():
                token = Token(INTEGER, num)
                return token

        current_char = text[self.pos]
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            print("errro")
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTGER"""
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(op.type)

        right = self.current_token
        self.eat(INTEGER)

        result = 0
        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value

        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        res = interpreter.expr()
        print(res)


if __name__ == '__main__':
    main()
    # interpreter = Interpreter("12 +3")
    # res = interpreter.expr()
    # print(res)
