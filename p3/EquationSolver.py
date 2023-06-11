import DSAStack
import DSAQueue

def _parseNextTerm(equation):
    infix = equation.split(" ")
    return infix

def _precedenceOf(operator):
    if(operator == '*' or '/'):
        precedence = 2
    elif(operator == '+' or '-'):
        precedence = 1
    return precedence

def _parseInfixToPostfix(equation):
    opStack = DSAStack.DSAStack()
    postfix = DSAQueue.shufflingQueue()
    infix = _parseNextTerm(equation)

    for i in range(len(infix)):
        term = infix[i]
        if(term == '('):
            opStack.push('(')
        elif(term == ')'):
            while(opStack.top() != '('):
                postfix.enqueue(opStack.pop())
            opStack.pop()
        elif (term == '+' or term == '-' or term == '*' or term == '/'):
            while((not opStack.isEmpty()) and (opStack.top() != '(') and (_precedenceOf(opStack.top()) >= _precedenceOf(term))):
                postfix.enqueue(opStack.pop())
            opStack.push(term)
        else:
            postfix.enqueue(float(term))

    while(not opStack.isEmpty()):
        postfix.enqueue(opStack.pop())

    return postfix

def _executeOperation(op, op1, op2):
    if(op == '*'):
        result = op2 * op1
    elif(op == '/'):
        result = op2 / op1
    elif(op == '+'):
        result = op2 + op1
    elif(op == '-'):
        result = op2 - op1
    return result

def _evaluatePostfix(postfixQueue):
    opStack = DSAStack.DSAStack()
    postfix = postfixQueue

    for i in range(postfix.count):
        term = postfix.queue[i]
        if(isinstance(term, float)):
            opStack.push(term)
        else:
            val1 = opStack.pop()
            val2 = opStack.pop()
            opStack.push(_executeOperation(term, val1, val2))

    result = opStack.top()
    return result

def solve(equation):
    postfix = _parseInfixToPostfix(equation)
    result = _evaluatePostfix(postfix)
    return result

if __name__ == '__main__':
    print(solve("( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )"))
