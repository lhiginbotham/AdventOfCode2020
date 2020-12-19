import itertools

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].rstrip()

rules = dict()
validationStrings = []
for line in inp:
    if ':' in line:
        ruleNum, ruleLogic = line.split(': ')
        ruleNum = int(ruleNum)
        rules[ruleNum] = ruleLogic
    elif len(line) > 0:
        validationStrings.append(line)


# compiledRules = { number: ["indRuleOne", "indRuleTwo", ...], number2.... }
compiledRules = dict()
def compileRule(rule):
    ruleSyntax = [] # ruleSyntax = [ [ruleOneNum, ruleTwoNum, ruleThreeNum], ..., ... ]
    requiredRules = set()
    global ruleBuilder # ugh, just to enable the capture...
    ruleBuilder = ''
    startedNewRule = True

    def addRule():
        global ruleBuilder
        if len(ruleBuilder) == 0:
            return
            
        ruleNum = int(ruleBuilder)
        ruleBuilder = ''
        ruleSyntax[-1].append(ruleNum)
        requiredRules.add(ruleNum)

    for c in rules[rule]:
        if c.isnumeric():
            if startedNewRule:
                ruleSyntax.append([])
                startedNewRule = False
            ruleBuilder += c
        elif c == '|':
            addRule()
            startedNewRule = True
        elif c.isalpha():
            compiledRules[rule] = [str(c)]
            return
        else:
            addRule()

    addRule()

    for r in requiredRules:
        if r not in compiledRules:
            return

    compiledRule = [] # compiledRule = [ "ruleStrOne", "ruleStrTwo", ... ]
    print(ruleSyntax)
    for independentRule in ruleSyntax:
        #compiledSubRule = []
        compiledSubRuleArrs = []
        for i in range(len(independentRule)):
            compiledSubRuleArrs.append(compiledRules[int(independentRule[i])])

        print("compiledSubRuleArrs")
        print(compiledSubRuleArrs)
        compiledIndependentRule = []
        
        # this is really slow, can prob memoize rule concatenations to fix it!
        for r in itertools.product(*compiledSubRuleArrs):
            print(r)
            ruleStr = ''
            for s in r:
                ruleStr += s
            print("rule str")
            print(ruleStr)
            compiledIndependentRule.append(ruleStr)

        for r in compiledIndependentRule:
            compiledRule.append(r)

    compiledRules[rule] = compiledRule
    print(compiledRule)

def compileRules():
    someRulesNeedCompiled = True
    while someRulesNeedCompiled:
        someRulesNeedCompiled = False
        for rule in rules.keys():
            if not rule in compiledRules:
                someRulesNeedCompiled = True
                compileRule(rule)

def validateAgainstRules(message, ruleSucceededCounts):
    for m in compiledRules[0]:
        if message == m:
            ruleSucceededCounts[0] += 1

compileRules()
ruleSucceededCounts = dict()
for r in rules.keys():
    ruleSucceededCounts[r] = 0

for st in validationStrings:
    validateAgainstRules(st, ruleSucceededCounts)

print(ruleSucceededCounts[0])