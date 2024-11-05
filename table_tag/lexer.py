import ply.lex as lex    # type: ignore

tokens = ('TABLE_OPEN', 'TABLE_CLOSE','TR_OPEN', 'TR_CLOSE','TD_OPEN', 'TD_CLOSE','CONTENT',)

t_TABLE_OPEN = r'<table>'
t_TABLE_CLOSE = r'</table>'
t_TR_OPEN = r'<tr>'
t_TR_CLOSE = r'</tr>'
t_TD_OPEN = r'<td>'
t_TD_CLOSE = r'</td>'
t_CONTENT = r'[^<]+'  
t_ignore = ' \t\n'

def t_error(t):
    #print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
<table>
    <tr>
        <td>Row 1, Col 1</td>
        <td>Row 1, Col 2</td>
    </tr>
    <tr>
        <td>Row 2, Col 1</td>
        <td>Row 2, Col 2</td>
    </tr>
</table>
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type,'->',tok.value)
