import ply.yacc as yacc # type: ignore
from lexer import tokens

def p_table(p):
    '''table : TABLE_OPEN rows TABLE_CLOSE'''
    print("Parsed a table with rows:")
    p[0] = p[2]  

def p_rows(p):
    '''rows : row rows
            | row'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]  
    else:
        p[0] = [p[1]]  

def p_row(p):
    '''row : TR_OPEN cells TR_CLOSE'''
    print("Parsed a row with cells:")
    p[0] = p[2]  

def p_cells(p):
    '''cells : cell cells
             | cell'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]  
    else:
        p[0] = [p[1]]  

def p_cell(p):
    '''cell : TD_OPEN CONTENT TD_CLOSE'''
    print(f"Parsed a cell: {p[2]}")
    p[0] = p[2] 

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

html_input = '''
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

parser.parse(html_input)

while True:
    try:
        s = input('table> ') 
    except EOFError:
        break  
    
    if s.lower() in ['exit', 'quit']: 
        print("Exiting the parser.")
        break
    
    if not s: 
        continue
    
    result = parser.parse(s)  
    print(result)  
