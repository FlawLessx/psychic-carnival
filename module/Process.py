from module.Buffer import Buffer
from module.LexicalAnalyzer import LexicalAnalyzer

class Process:
    def process(self, Buffer, Analyzer, code, lang):

        token = []
        tokenType = []
        lexeme = []
        row = 1
        column = []
        result = []

        # Tokenize and reload of the buffer
        for i in code:
            t, tType,lex, lin, col, res = Analyzer.tokenize(code=i, lang=lang, row=row)
            token += t
            tokenType += tType
            lexeme += lex
            column += col
            row += 1
            result += res

        return token, tokenType, lexeme, row, column, result

