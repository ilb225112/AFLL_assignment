# parser.py
import ply.yacc as yacc
from lexer import tokens

def p_heading(p):
    '''heading : heading1
                | heading2
                | heading3
                | heading4
                | heading5
                | heading6 
                | heading heading
                '''

def p_heading1(p):
    '''heading1 : HEADING1 CONTENT CLOSE_HEADING1'''
    print(f"Heading 1: {p[2]}")

def p_heading2(p):
    '''heading2 : HEADING2 CONTENT CLOSE_HEADING2'''
    print(f"Heading 2: {p[2]}")

def p_heading3(p):
    '''heading3 : HEADING3 CONTENT CLOSE_HEADING3'''
    print(f"Heading 3: {p[2]}")

def p_heading4(p):
    '''heading4 : HEADING4 CONTENT CLOSE_HEADING4'''
    print(f"Heading 4: {p[2]}")

def p_heading5(p):
    '''heading5 : HEADING5 CONTENT CLOSE_HEADING5'''
    print(f"Heading 5: {p[2]}")

def p_heading6(p):
    '''heading6 : HEADING6 CONTENT CLOSE_HEADING6'''
    print(f"Heading 6: {p[2]}")


def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")


# Build the parser
parser = yacc.yacc()

# Example data to test the parser
data = '''
<h1>This is a heading</h1>
<h2>This is a subheading</h2>
<h3>This is a smaller heading</h3>
<h4>This is a fourth heading</h4>
<h5>This is a fifth heading</h5>
<h6>This is a sixth heading</h6>
'''

# Parse the input data
parser.parse(data)

'''
Valid:
<h1>Heading 1 content</h1>
<h2>Heading 2 content</h2>

<h3>Another heading</h3>
<h4>Yet another heading</h4>

Invalid:
<h1>Heading without closing tag

<h2>Heading content</h3>

'''