import ply.yacc as yacc
from lexer import tokens

def p_img_tag(p):
    '''img_tag : IMG_TAG SRC_ATTR ALT_ATTR CLOSE_TAG'''
    src_value = p[2].split('"')[1]  
    alt_value = p[3].split('"')[1] 
    print(f"Image Source: {src_value}, Alt Text: {alt_value}")

def p_img_tag_without_alt(p):
    '''img_tag : IMG_TAG SRC_ATTR CLOSE_TAG'''
    src_value = p[2].split('"')[1]  
    print(f"Image Source: {src_value}, Alt Text: None")

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

while True:
    try:
        s = input('body> ')  
    except EOFError:
        break  
    if s.lower() in ['exit', 'quit']:  
        print("Exiting the parser.")
        break
    if not s:
        continue  
    result = parser.parse(s) 

#parser.parse('<img src="sdkcksd" alt="dncjnsc">' )

'''
GRAMMAR - 
img_tag : IMG_TAG src_attr alt_attr CLOSE_TAG
src_attr : SRC_ATTR
alt_attr : ALT_ATTR
'''