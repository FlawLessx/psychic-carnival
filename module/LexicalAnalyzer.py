import re


class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, row ,code, lang):
        result = []

        rules = [
            ('HEADER', r'#include <(.*?)>' if lang == 'c' or lang == 'cpp' else r'import .*'),
            ('BOOLEAN_CONST', r'(true|false)' if lang == 'c' or lang == 'cpp' else r'(True|False)'),
            ('CONTINUE', r'continue'),
            ('COMMENT', r'//.*' if lang == 'c' or lang == 'cpp' else r'#.*'),
            ('BREAK', r'break'),
            ('CLASS', r'class'),
            ('NAMESPACE', r'using namespace .*'),
            ('COLON', r':'),
            ('BOOLEAN', r'bool'),
            ('MAIN', r'main'),          # main
            ('INT', r'int'),            # int
            ('FLOAT', r'float'),        # float
            ('IF', r'if'),              # if
            ('ELSE', r'else'),          # else
            ('WHILE', r'while'),        # while
            ('READ', r'read'),          # read
            ('PRINT', r'print'),        # print
            ('LBRACKET', r'\('),        # (
            ('RBRACKET', r'\)'),        # )
            ('LBRACE', r'\{'),          # {
            ('RBRACE', r'\}'),          # }
            ('COMMA', r','),            # ,
            ('PCOMMA', r';'),           # ;
            ('EQ', r'=='),              # ==
            ('NE', r'!='),              # !=
            ('LE', r'<='),              # <=
            ('GE', r'>='),              # >=
            ('OR', r'\|\|'),            # ||
            ('AND', r'&&'),             # &&
            ('ATTR', r'\='),            # =
            ('LT', r'<'),               # <
            ('GT', r'>'),               # >
            ('PLUS', r'\+'),            # +
            ('MINUS', r'-'),            # -
            ('MULT', r'\*'),            # *
            ('DIV', r'\/'),             # /
            ('ID', r'[a-zA-Z]\w*'),     # IDENTIFIERS
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            ('INTEGER_CONST', r'\d(\d)*'),          # INT
            ('NEWLINE', r'\n'),         # NEW LINE
            ('SKIP', r'[ \t]+'),
            ('STRING_CONST', r'\".*?\"'),
            ('CHAR_CONST', r"\'.*?\'"),
        ]

        rulesType = [
            ('MAIN', 'IDENTIFIER'),          # main
            ('INT', 'KEYWORD'),            # int
            ('FLOAT', 'KEYWORD'),        # float
            ('IF', 'KEYWORD'),              # if
            ('ELSE', 'KEYWORD'),          # else
            ('WHILE', 'KEYWORD'),        # while
            ('READ',  'KEYWORD'),          # read
            ('PRINT',  'KEYWORD'),        # print
            ('LBRACKET',  'PUNCTUATION'),        # (
            ('RBRACKET', 'PUNCTUATION'),        # )
            ('LBRACE', 'PUNCTUATION'),          # {
            ('RBRACE',  'PUNCTUATION'),          # }
            ('COMMA',  'PUNCTUATION'),            # ,
            ('PCOMMA',  'PUNCTUATION'),           # ;
            ('EQ', 'OPERATOR'),              # ==
            ('NE', 'OPERATOR'),              # !=
            ('LE', 'OPERATOR'),              # <=
            ('GE', 'OPERATOR'),              # >=
            ('OR', 'OPERATOR'),            # ||
            ('AND', 'OPERATOR'),             # &&
            ('ATTR', 'OPERATOR'),            # =
            ('LT', 'OPERATOR'),               # <
            ('GT','OPERATOR'),               # >
            ('PLUS','OPERATOR'),            # +
            ('MINUS', 'OPERATOR'),            # -
            ('MULT', 'OPERATOR'),            # *
            ('DIV', 'OPERATOR'),             # /
            ('ID',  'IDENTIFIER'),     
            ('FLOAT_CONST', 'LITERALS'),   
            ('INTEGER_CONST', 'LITERALS'), 
            ('NEWLINE',  'PUNCTUATION'),
            ('SKIP',  'PUNCTUATION'),
            ('HEADER',  'KEYWORD'),
            ('STRING_CONST', 'LITERALS'),
            ('COMMENT', 'PUNCTUATION'),
            ('BOOLEAN_CONST', 'LITERALS'),
            ('CHAR_CONST', 'LITERALS'),
            ('CLASS', 'KEYWORD'),
            ('CONTINUE', 'KEYWORD'),
            ('BREAK', 'KEYWORD'),
            ('NAMESPACE', 'KEYWORD'),
            ('BOOLEAN', 'KEYWORD'),
            ('COLON', 'PUNCTUATION')
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        # Lists of output for the program
        token = []
        tokenType = []
        lexeme = []
        column = []

        # It analyzes the code to find the lexemes and their respective Tokens
        for m in re.finditer(tokens_join, code):
            token_name = m.lastgroup
            token_lexeme = m.group(token_name)

            if token_name == 'NEWLINE':
                lin_start = m.end()
                self.lin_num += 1
            elif token_name == 'SKIP':
                continue
            elif token_name == 'MISMATCH':
                raise RuntimeError('%r unexpected on line %d' %
                                   (token_lexeme, self.lin_num))
            else:
                col = m.start() - lin_start
                column.append(col)
                token.append(token_name)
                lexeme.append(token_lexeme)

                for i in rulesType:
                    if i[0] == token_name:
                        tokenType = i[1]
                        break

                # Tambahkan ke hasil
                result.append('Token = {0}, Type = {1}, Lexeme = \'{2}\', Row = {3}, Column = {4}'.format(
                    token_name, tokenType, token_lexeme, row, col))

        return token, tokenType, lexeme, row, column, result
