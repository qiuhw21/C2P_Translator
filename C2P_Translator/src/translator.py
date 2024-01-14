output=""
def process_program(program):
    _,declaration_list=program
    process_declaration_list(declaration_list)
    return output

def process_declaration_list(declaration_list):
    for declaration in declaration_list:
        process_declaration(declaration)

def process_declaration(declaration):
    retraction="\t"
    declaration_type = declaration[0]
    if declaration_type == 'var_declaration':
        process_var_declaration(declaration[1],'true',retraction)
    elif declaration_type == 'function_declaration':
        process_function_declaration(declaration)
    elif declaration_type == 'function_definition':
        process_function_definition(declaration,retraction)
    elif declaration_type == 'array_declaration_init':
        process_array_declaration_init(declaration,retraction)
    elif declaration_type=='array_declaration':
        process_array_declaration(declaration,retraction)
    # Add more cases for other declaration types as needed...

def process_array_declaration(declaration,retraction):
    global output
    _, type_specifier, identifier, expression = declaration
    output+=f"{retraction}{identifier} = [0]* "
    process_expression(expression)
    output+="\n"

def process_var_declaration(declaration,flag,retraction):
    global output
    var_type=declaration[0]
    if var_type=='var_direct_declaration':
        if flag=='true':
            # print(f"{retraction}{declaration[2]}")
            output+=f"{retraction}{declaration[2]}\n"
    elif var_type=='var_pointer_declaration':
        if flag=='true':
            # print(f"{retraction}{declaration[3]}")
            output+=f"{retraction}{declaration[3]}\n"
    else:
        expression=declaration[3]
        # print(f"{retraction}{declaration[2]} = ",end="")
        output+=f"{retraction}{declaration[2]} = "
        process_expression(expression)
        # print('')
        output+=f"\n"

# need complemented
def process_expression(expression):
    global output
    if expression[0]=='assignment_expression_identifier':
        # print(f"{expression[1]} = ",end="")
        output+=f"{expression[1]} = "
        process_expression(expression[2])
    elif expression[0]=='assignment_expression_array_access':
        process_array_access(expression[1])
        # print(f" = ",end="")
        output+=f" = "
        process_expression(expression[2])
    elif expression[0]=='binary_expression':
        process_expression(expression[2])
        if expression[1]=="&&":
            op="and"
        elif expression[1]=="||":
            op="or"
        elif expression[1]=="!":
            op="not"
        else:
            op=expression[1]
        # print(f" {expression[1]} ",end="")
        output+=f" {op} "
        process_expression(expression[3])
    elif expression[0]=='unary_expression':
        if expression[1]=='-' or expression[1]=='!':
            # print(f"{expression[1]} ",end="")
            output+=f"{expression[1]} "
            process_expression(expression[2])
        elif expression[2]=="++":
            output+=f"{expression[1]} += 1"
        elif expression[1]=="++":
            output+=f"{expression[2]} += 1"
        elif expression[2]=="--":
            output+=f"{expression[1]} -= 1"
        elif expression[1]=="--":
            output+=f"{expression[2]} -= 1"    
        else:
            # print(f"{expression[1]} {expression[2]}",end="")
            output+=f"{expression[1]} {expression[2]}"
    elif expression[0]=='term':
        # print(f"{expression[1]}",end="")
        output+=f"{expression[1]}"
    elif expression[0]=='paren_expression':
        # print(f"(",end="")
        output+=f"("
        process_expression(expression[1])
        # print(f")",end="")
        output+=f")"
    elif expression[0]=='function_call':
        # print(f"{expression[1]}(",end="")
        if expression[1]=="printf":
            op="print"
        elif expression[1]=="strlen":
            op="len"
        else:
            op=expression[1]
        output+=f"{op}("
        process_argument_list(expression[2])
        # print(f")",end="")
        output+=f")"
    elif expression[0]=='array_access':
        process_array_access(expression)

def process_array_access(array_access):
    global output
    # print(f"{array_access[1]}[",end="")
    output+=f"{array_access[1]}["
    process_expression(array_access[2])
    # print(f"]",end="")
    output+=f"]"


def process_argument_list(argument_list):
    global output
    i=0
    for expression in argument_list:
        i+=1
        process_expression(expression)
        if i<len(argument_list):
            # print(', ',end="") 
            output+=', '      

def process_expression_statement(expression_statement):
    _, expression = expression_statement
    process_expression(expression)

def process_function_declaration(declaration):
    global output
    # print(f"def {declaration[2]}(",end="")
    output+=f"def {declaration[2]}("
    process_param_list(declaration[3])
    # print(f");")
    output+=f");\n"

def process_function_definition(declaration,retraction):
    global output
    _, type_specifier, identifier, param_list, compound_statement = declaration
    # print(f"def {identifier}(",end="")
    output+=f"def {identifier}("
    process_param_list(param_list)
    # print(f"):")
    output+=f"):\n"

    process_compound_statement(compound_statement,retraction)

def process_compound_statement(compound_statement,retraction):
    _, statement_list= compound_statement
    process_statement_list(statement_list,retraction)

def process_statement_list(statement_list,retraction):
    for statement in statement_list:
        process_statement(statement,retraction)

def process_statement(statement,retraction):
    global output
    statement_type = statement[0]
    if statement_type == 'expression_statement':
        # print(retraction,end="")
        output+=f"{retraction}"
        process_expression(statement[1])
        # print("")
        output+=f"\n"
    elif statement_type == 'compound_statement':
        process_compound_statement(statement,retraction)
    elif statement_type == 'if_statement':
        process_if_statement(statement,retraction)
    elif statement_type == 'if_else_statement':
        process_if_else_statement(statement,retraction)
    elif statement_type == 'for_statement':
        process_for_statement(statement,retraction)
    elif statement_type == 'while_statement':
        process_while_statement(statement,retraction)
    elif statement_type == 'return_statement':
        process_return_statement(statement,retraction)
    elif statement_type == 'continue_statement':
        process_continue_statement(statement,retraction)
    elif statement_type == 'break_statement':
        process_break_statement(statement,retraction)
    elif statement_type == 'var_declaration':
        process_var_declaration(statement[1],'false',retraction)
    elif statement_type == 'array_declaration_init':
        process_array_declaration_init(statement,retraction)
    elif statement_type=='array_declaration':
        process_array_declaration(statement,retraction)

def process_array_declaration_init(declaration,retraction):
    global output
    _, type, type_specifier, identifier, *rest = declaration
    if type == '1':
        array_list = rest[1]
        # print(f"{retraction}{identifier} = ",end="")
        # print("{",end="")
        output+=f"{retraction}{identifier} = "
        output+="["
        process_array_list(array_list)
        # print("}")
        output+="]\n"
    elif type == '2':  # Array declaration with initialization
        array_list = rest[0]
        # print(f"{retraction}{identifier} = ",end="")
        output+=f"{retraction}{identifier} = "
        # print("{",end="")
        output+="["
        process_array_list(array_list)
        # print("}")
        output+="]\n"
    elif type =='3':
        # print(f"{retraction}{identifier} = {rest[0]}")
        output+=f"{retraction}{identifier} = {rest[0]}\n"
    else:
        # print(f"{retraction}{identifier} = {rest[0]}")
        output+=f"{retraction}{identifier} = {rest[0]}\n"

def process_array_list(array_list):
    global output
    i=0
    for expression in array_list:
        process_expression(expression)
        i+=1
        if i<len(array_list):
            # print(',',end="")
            output+=','


def process_if_statement(statement,retraction):
    global output
    # print(f"{retraction}if ",end="")
    output+=f"{retraction}if "
    process_expression(statement[1])
    # print(f":")
    output+=f":\n"
    retraction+='\t'
    process_statement(statement[2],retraction)

def process_if_else_statement(statement,retraction):
    global output
    # print(f"{retraction}if ",end="")
    output+=f"{retraction}if "
    process_expression(statement[1])
    # print(f":")
    output+=f":\n"
    retraction1=retraction+'\t'
    process_statement(statement[2],retraction1)
    # print(f"{retraction}else")
    output+=f"{retraction}else:\n"
    process_statement(statement[3],retraction1)

def process_while_statement(statement,retraction):
    global output
    # print(f"{retraction}while ",end="")
    output+=f"{retraction}while "
    process_expression(statement[1])
    # print(f":")
    output+=f":\n"
    retraction+='\t'
    process_statement(statement[2],retraction)

def process_for_statement(statement,retraction):
    global output
    if statement[1][0]=='for_expression_statement':
        # print(retraction,end="")
        output+=retraction
        process_expression_statement(statement[1][1])
        # print("")
        output+=f"\n"
        # print(f"{retraction}while ",end="")
        output+=f"{retraction}while "
        process_expression_statement(statement[1][2])

        # print(f":")
        output+=f":\n"
        retraction+='\t'
        
        process_statement(statement[1][4],retraction)
        # print(retraction,end="")
        output+=retraction
        process_expression(statement[1][3])
        # print("")
        output+=f"\n"
    elif statement[1][0]=='for_var_declaration':
        process_var_declaration(statement[1][1][1],'false',retraction)
        # print(f"{retraction}while ",end="")
        output+=f"{retraction}while "
        process_expression_statement(statement[1][2])

        # print(f":")
        output+=f":\n"
        retraction+='\t'
        process_statement(statement[1][4],retraction)
        # print(retraction,end="")
        output+=retraction
        process_expression(statement[1][3])
        # print("")
        output+=f"\n"
def process_return_statement(statement,retraction):
    global output
    # print(f"{retraction}return ",end="")
    output+=f"{retraction}return "
    process_expression(statement[1])
    # print("")
    output+=f"\n"

def process_continue_statement(statement,retraction):
    global output
    # print(f"continue")
    output+=f"{retraction}continue\n"

def process_break_statement(statement,retraction):
    global output
    # print(f"break")
    output+=f"{retraction}break\n"





def process_param_list(param_list):
    global output
    i=0
    for param in param_list:
        i+=1
        process_param(param)
        # param splited by ','
        if i<len(param_list):
            # print(',',end="")
            output+=','

def process_param(param):
    global output
    _,type_specifier, *rest = param
    if len(rest) == 1:  # Regular parameter
        identifier = rest[0]
        # print(f"{identifier}",end="")
        output+=f"{identifier}"
    elif len(rest) == 3:  # Array parameter
        identifier, _ , _= rest
        # print(f"{identifier}",end="")
        output+=f"{identifier}"
    elif len(rest) == 2:  # Pointer parameter
        _, _, identifier = rest
        # print(f"{identifier}",end="")
        output+=f"{identifier}"

# Similar functions can be added for other declaration types...



# You can continue adding functions for processing other parts of the AST




    # Add more cases for other statement types as needed...




