class SM:
    def start(self):
        self.state = self.startState

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

class Tokenizer(SM):
    def __init__(self):
        self.tokens = []
        self.singletokens = ['(', ')', '+', '-', '*', '/', '=']
        self.startState = 0
    def getNextValues(self, state, inp):
        print "RAN GET NEXT VALUES"
        print state
        print inp
        for token in self.singletokens:
            if inp == token:
                self.tokens.append(token)
            else:
                pass
        return (state, inp)



def tokenize(inputString):
    a = Tokenizer()
    a.transduce(inputString)

a = Tokenizer()
