inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

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
    total += recSolve(prob, [0]) 
print(total)
