import ply.yacc as yacc  # type: ignore
from lexer import tokens

# Parsing rules
def p_form(p):
    '''form : FORM_OPEN inputs FORM_CLOSE'''
    print("Parsed a form.")

def p_inputs(p):
    '''inputs : input inputs
              | input'''
    pass  

def p_input(p):
    '''input : INPUT_TEXT 
             | INPUT_PASSWORD 
             | INPUT_SUBMIT'''
    handle_input(p[1])  
    
def handle_input(input_tag):
    if input_tag.startswith('<input type="text"'):
        print("Parsed a text input for username.")
    elif input_tag.startswith('<input type="password"'):
        print("Parsed a password input.")
    elif input_tag.startswith('<input type="submit"'):
        print("Parsed a submit button.")
    
    handle_attributes(input_tag)

def handle_attributes(input_tag):
    import re
    attr_matches = re.findall(r'(\w+)="([^"]+)"', input_tag)
    for attr, val in attr_matches:
        print(f"Parsed attribute: {attr}, value: {val}")

def p_attr(p):
    '''attr : ATTR'''
    print(f"Parsed attribute: {p[1]}")

def p_error(p):
    print(f"Syntax error at '{p.value}'" if p else "Syntax error at EOF")

parser = yacc.yacc()

html_input = '''
<form action="/submit" method="post">
  <input type="text" name="username">
  <input type="password" name="password">
  <input type="submit" value="Submit">
</form>
'''

result = parser.parse(html_input)

while True:
    try:
        s = input('form> ')  
    except EOFError:
        break  
    if s.lower() in ['exit', 'quit']:  
        print("Exiting the parser.")
        break
    if not s:
        continue  
    result = parser.parse(s)
