from module.Buffer import Buffer
from module.LexicalAnalyzer import LexicalAnalyzer

class Process:
    def process(self, path, Buffer, Analyzer):

        token = []
        lexeme = []
        row = []
        column = []
        result = []

        # Tokenize and reload of the buffer
        for i in Buffer.load_buffer(path=path):
            t, lex, lin, col, res = Analyzer.tokenize(i)
            token += t
            lexeme += lex
            row += lin
            column += col
            result += res

        return token, lexeme, row, column, result

