def parse(tokens):
    print tokens, "TOKEN LIST"
    def parseExp():
        tokensLeft = tokens[:]
        token = tokensLeft.pop(0)
        if numberTok(token) == True:
            a = Number(float(token))
            return a
        if variableTok(token) == True:
	    b = Variable(token)
            return b
        if token == '(':
            left = parseExp()
            operator = tokensLeft.pop(0)
            right = parseExp()
            tokensLeft.pop(0)
            if operator == '+'
                return Sum(left,right)
            if operator == '-'
                return Diff(left,right)
            if operator == '/'
                return Quit(left,right)
            if operator == '*'
                return Prod(left,right)
            if operator == '='
                return Assign(left,right)
        tokensLeft = tokens[:]
    return parseExp()
