import ply.lex as lex # type: ignore

tokens = ('FORM_OPEN', 'FORM_CLOSE', 'INPUT_TEXT', 'INPUT_PASSWORD', 'INPUT_SUBMIT', 'ATTR', 'VALUE')

t_FORM_OPEN = r'<form[^>]*>'                    #accepts form id="abcd" action="submit"... so [^>]* 0 or more occurences of char class not having >
t_FORM_CLOSE = r'</form>'
t_INPUT_TEXT = r'<input\s+type="text"[^>]*>'    #\s+ => space to the power + (1or more occurences)
t_INPUT_PASSWORD = r'<input\s+type="password"[^>]*>'
t_INPUT_SUBMIT = r'<input\s+type="submit"[^>]*>'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it with some HTML form data
data = '''
<form action="/submit" method="post">
  <input type="text" name="username">
  <input type="password" name="password">
  <input type="submit" value="Submit">
</form>
'''

# Tokenize
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
