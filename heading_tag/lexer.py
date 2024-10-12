# lexer.py
import ply.lex as lex

# List of token names
tokens = (
    'HEADING1',               # Matches <h1>...</h1>
    'HEADING2',               # Matches <h2>...</h2>
    'HEADING3',               # Matches <h3>...</h3>
    'HEADING4',               # Matches <h4>...</h4>
    'HEADING5',               # Matches <h5>...</h5>
    'HEADING6',               # Matches <h6>...</h6>
    'CLOSE_HEADING1',         # Matches </h1>
    'CLOSE_HEADING2',         # Matches </h2>
    'CLOSE_HEADING3',         # Matches </h3>
    'CLOSE_HEADING4',         # Matches </h4>
    'CLOSE_HEADING5',         # Matches </h5>
    'CLOSE_HEADING6',         # Matches </h6>
    'CONTENT',                # Matches the content of the heading
)

# Regular expression rules for simple tokens
t_HEADING1 = r'<h1>'
t_HEADING2 = r'<h2>'
t_HEADING3 = r'<h3>'
t_HEADING4 = r'<h4>'
t_HEADING5 = r'<h5>'
t_HEADING6 = r'<h6>'
t_CLOSE_HEADING1 = r'</h1>'
t_CLOSE_HEADING2 = r'</h2>'
t_CLOSE_HEADING3 = r'</h3>'
t_CLOSE_HEADING4 = r'</h4>'
t_CLOSE_HEADING5 = r'</h5>'
t_CLOSE_HEADING6 = r'</h6>'
t_CONTENT = r'[^<]+'  # Matches any text that does not contain a '<'

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule for newlines (line terminators)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Example data to test the lexer
data = '''
<h1>This is a heading</h1>
<h2>This is a subheading</h2>
<h3>This is a smaller heading</h3>
<h4>This is a fourth heading</h4>
<h5>This is a fifth heading</h5>
<h6>This is a sixth heading</h6>
'''

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
