import ply.lex as lex

tokens = ('FORM_OPEN', 'FORM_CLOSE', 'INPUT_TEXT', 'INPUT_PASSWORD', 'INPUT_SUBMIT', 'ATTR', 'VALUE')

t_FORM_OPEN = r'<form[^>]*>'
t_FORM_CLOSE = r'</form>'
t_INPUT_TEXT = r'<input\s+type="text"[^>]*>'
t_INPUT_PASSWORD = r'<input\s+type="password"[^>]*>'
t_INPUT_SUBMIT = r'<input\s+type="submit"[^>]*>'
t_ATTR = r'[a-zA-Z-]+="[^"]*"'
t_VALUE = r'[^<>]+'

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
<form action="/submit" method="post">
  <input type="text" name="username">
  <input type="password" name="password">
  <input type="submit" value="Submit">
</form>
'''

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
