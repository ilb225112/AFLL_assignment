import ply.lex as lex

tokens = ('IMG_TAG','SRC_ATTR','ALT_ATTR','CLOSE_TAG',)

t_IMG_TAG = r'<img'
t_SRC_ATTR = r'src="([^"]*)"'
t_ALT_ATTR = r'alt="([^"]*)"'
t_CLOSE_TAG = r'>'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data='''
<img src="sjajsj" alt="kkkk" >
'''
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok)