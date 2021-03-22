# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis


INTEGER, PLUS, MINUS, MULTIPLE, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTI', 'DIVIDE', 'EOF'


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
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text)-1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLE, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIVIDE, '/')

            self.error()

        return Token(EOF, None)

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
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            result = left.value + right.value
        elif op.type == MINUS:
            result = left.value - right.value
        elif op.type == MULTIPLE:
            result = left.value * right.value
        else:
            result = left.value / right.value

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
