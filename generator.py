from grammar import Grammar, S

class Generator:

    def __init__(self, grammar: Grammar, vocab):
        """
        rules(Grammar) contains the allowed 
        """
        self.grammar = grammar
        self.vocab = vocab
    
    def apply_rule(self, j):
        return

    def break_down(self, i):
        for j in i:

            if j in self.grammar.Os:
                j = self.apply_rule(j)



            while(type(j) != str):
                j = self.break_down(j)

    def produce_sentence(self):
        sentence = [S()]
        for i in sentence:
            while(type(i) != str):
                i = self.break_down(i)


