inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

def insertParensToForceAdditionHigherPrecedence(_expr):
    expr = [c for c in _expr]
    i = 0
    while i < len(expr):
        if expr[i] == '+':
            # find left paren place
            lParenPlacementIdx = 0
            rParenCount = 0
            sawNumeric = False
            for j in range(i - 1, -1, -1):
                if sawNumeric and not expr[j].isnumeric():
                    lParenPlacementIdx = j
                    break
                if expr[j] == ')':
                    rParenCount += 1
                elif expr[j] == '(':
                    rParenCount -= 1
                    if rParenCount == 0:
                        lParenPlacementIdx = j
                        break
                elif rParenCount == 0 and expr[j].isnumeric():
                    sawNumeric = True

            # find right paren place
            rParenPlacementIdx = len(expr)
            lParenCount = 0
            sawNumeric = False
            for j in range(i + 1, len(expr)):
                if sawNumeric and not expr[j].isnumeric():
                    rParenPlacementIdx = j
                    break
                if expr[j] == '(':
                    lParenCount += 1
                elif expr[j] == ')':
                    lParenCount -= 1
                    if lParenCount == 0:
                        rParenPlacementIdx = j
                        break
                elif lParenCount == 0 and expr[j].isnumeric():
                    sawNumeric = True

            # place parens
            expr.insert(rParenPlacementIdx, ')')
            expr.insert(lParenPlacementIdx, '(')
            i += 1
        i += 1
    return ''.join(expr)

def recSolve(expr, cursor):
    leftOperand = ''
    op = ''
    rightOperand = ''
    while cursor[0] < len(expr):
        if expr[cursor[0]] == '(':
            if len(op) == 0:
                cursor[0] += 1
                leftOperand = str(recSolve(expr, cursor))
                cursor[0] += 1
                continue
            else:
                cursor[0] += 1
                rightOperand = str(recSolve(expr, cursor))
                cursor[0] += 1
                continue
        elif expr[cursor[0]] in '+*':
            if len(op) != 0:
                leftOperand = str(int(leftOperand) + int(rightOperand)) if op == '+' else str(int(leftOperand) * int(rightOperand))
                op = ''
                rightOperand = ''
            op = expr[cursor[0]]
            cursor[0] += 1
            continue
        elif expr[cursor[0]].isnumeric():
            if len(leftOperand) == 0:
                leftOperand += expr[cursor[0]]
            else:
                rightOperand += expr[cursor[0]]
            cursor[0] += 1
            continue
        elif expr[cursor[0]] == ')':
            if len(op) != 0:
                leftOperand = str(int(leftOperand) + int(rightOperand)) if op == '+' else str(int(leftOperand) * int(rightOperand))
            op = ''
            rightOperand = ''
            return int(leftOperand)
        else:
            cursor[0] += 1
    if len(op) != 0:
        leftOperand = str(int(leftOperand) + int(rightOperand)) if op == '+' else str(int(leftOperand) * int(rightOperand))
        op = ''
        rightOperand = ''
    return int(leftOperand)

total = 0
for prob in inp:
    print(prob)
    prob = insertParensToForceAdditionHigherPrecedence(prob)
    print(prob)
    total += recSolve(prob, [0]) 
print(total)
