
import grammar as g
import generator as gen

rule1 = g.Rule(g.S, [(g.NP, 0), (g.VP, 0)])
rule2 = g.Rule(g.NP, [(g.Det, 1), (g.Adj, 1), (g.N, 0), (g.PP, 1)])
rule3 = g.Rule(g.VP, [(g.V, 0), (g.NP, 1), (g.PP, 1)])
rule4 = g.Rule(g.PP, [(g.P, 0), (g.NP, 0)])
rule5 = g.Rule(g.AdjP, [(g.Deg, 1), (g.Adj, 0), (g.PP, 1)])
rule6 = g.Rule(g.AdvP, [(g.Adv, 0), (g.Deg, 1)])

gram = g.Grammar([rule1, rule2, rule3, rule4, rule5, rule6])

vocab = []

generator = gen(gram, vocab)


















# S -> NP VP: A sentence consists of a noun phrase (NP) followed by a verb phrase (VP).

# NP -> (Det) (Adj) N (PP): A noun phrase consists of an optional determiner (Det), followed by zero or more adjectives (Adj), a noun (N), and an optional prepositional phrase (PP).

# VP -> V (NP) (PP): A verb phrase consists of a verb (V), optionally followed by a noun phrase (NP) and/or a prepositional phrase (PP).

# PP -> P NP: A prepositional phrase consists of a preposition (P) followed by a noun phrase (NP).

# AdjP -> (Deg) Adj (PP): An adjective phrase consists of an optional degree word (Deg), an adjective (Adj), and an optional prepositional phrase (PP).

# AdvP -> Adv (Deg): An adverb phrase consists of an adverb (Adv) and an optional degree word (Deg).
