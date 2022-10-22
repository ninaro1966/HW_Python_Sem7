import Model, View
def operation(list, i, oper):
    if list[i] == oper:
        list[i - 1] = Model.opSelect.get(oper)(int(list[i - 1]),int(list[i + 1]))
        deleteElement(list, i)
        return True
    return False

def deleteElement(string, i):
    string. pop(i)
    string. pop(i)

def calculate(list: list):
    while len(list) > 1:
        if '*' in list or '/' in list:
            for i in range(len(list)):
                if operation(list, i, '*'): break
                if operation(list, i, '/'): break

        elif '+' in list or '-' in list:
            for i in range(len(list)):
                if operation(list, i, '+'): break
                if operation(list, i, '-'): break
    return  list

def sliceByParentheses(expresssion: list):
    open_par, close_par = None, None
    for index, item in enumerate(expresssion):
        if item == "(": open_par = index
        elif item == ")": close_par = index
        if open_par != None and close_par != None:
            expression1 = expresssion[:open_par]
            expression2 = calculate(expresssion[open_par+1:close_par])
            expression3 = expresssion[close_par+1:]
            expresssion = []
            expresssion. extend(expression1)
            expresssion. extend(expression2)
            expresssion. extend(expression3)
            break
    return expresssion

def solutionExpression(expression: str):
    expression = Model. stringToList(expression)
    while   len(expression) > 1:
        # print(expression)
        if ('(' in expression) and (')' in expression):
            expression = sliceByParentheses(expression)
        else:
            expression = calculate(expression)
    Model.result = expression[0]
    View. printResult()

# sliceByParentheses('(1+3*(4-5*2) +10)/2')