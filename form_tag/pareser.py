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
    
def p_error(p):
    if p:
        print(f"Syntax error at ")
    else:
        print("Syntax error at EOF")
    raise SyntaxError("Parsing halted due to syntax error.")

parser = yacc.yacc()

html_input = '''
<form action="/submit" method="post">
  <input type="text" name="username">
  <input type="password" name="password">
  <input type="submit" value="Submit">
</form>
'''

try:
    result = parser.parse(html_input)
except SyntaxError as e:
    print(e)
    
    
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
    
    try:
        result = parser.parse(s)
    except SyntaxError as e:
        print(e)
        continue

'''
Valid Examples:
<form action="/submit" method="post">
  <input type="text" name="username">
  <input type="password" name="password">
  <input type="submit" value="Submit">
</form>

<form action="/login">
  <input type="text" name="user">
</form>

Invalid Examples:
<form action="/submit" method="post">
  <input type="text" name="username">
  <input type="submit" value="Submit">

<form>
  <input type="password" name="password"
  <input type="submit" value="Submit">
</form>
'''
