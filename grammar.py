class Grammar:

    def __init__(self, rules):
        """
        rules: list of Rule
        """
        self.rules = rules
        Os = self.getOs()
    
    def get_Os(self):
        Os = set()
        for rule in self.rules:
            Os.append(rule.getO())
        return Os

class Rule:
    def __init__(self, O, PS):
        """
        O is the part(s) of speach
        PS is a list of tuples(POS, boolean(optionality is true or false))
        """
        self.O = O
        self.PS = PS
    
    def getO(self):
        return self.O


class S:
    def __init__(self):
        return

class NP:
    def __init__(self):
        return

class VP:
    def __init__(self):
        return

class PP:
    def __init__(self):
        return

class P:
    def __init__(self):
        return

class AdjP:
    def __init__(self):
        return

class AdvP:
    def __init__(self):
        return

class Det:
    def __init__(self):
        return
    
class Adj:
    def __init__(self):
        return
    
class Adv:
    def __init__(self):
        return

class N:

    def __init__(self):
        return

class V:
    def __init__(self):
        return
    
class Deg:
    def __init__(self):
        return





# S -> NP VP: A sentence consists of a noun phrase (NP) followed by a verb phrase (VP).

# NP -> (Det) (Adj) N (PP): A noun phrase consists of an optional determiner (Det), followed by zero or more adjectives (Adj), a noun (N), and an optional prepositional phrase (PP).

# VP -> V (NP) (PP): A verb phrase consists of a verb (V), optionally followed by a noun phrase (NP) and/or a prepositional phrase (PP).

# PP -> P NP: A prepositional phrase consists of a preposition (P) followed by a noun phrase (NP).

# AdjP -> (Deg) Adj (PP): An adjective phrase consists of an optional degree word (Deg), an adjective (Adj), and an optional prepositional phrase (PP).

# AdvP -> Adv (Deg): An adverb phrase consists of an adverb (Adv) and an optional degree word (Deg).
