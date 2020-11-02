from module.Buffer import Buffer
from module.LexicalAnalyzer import LexicalAnalyzer

class Process:
    def process(self, Buffer, Analyzer, code):

        token = []
        tokenType = []
        lexeme = []
        row = []
        column = []
        result = []

        # Tokenize and reload of the buffer
        for i in code:
            t, tType,lex, lin, col, res = Analyzer.tokenize(i)
            token += t
            tokenType += tType
            lexeme += lex
            row += lin
            column += col
            result += res

        return token, tokenType, lexeme, row, column, result

