# RussSentenceGen
Generating Grammatically correct Russian sentences from vocab lists

based on a chompskian framework of syntax trees
starting with word order then later implimenting derivations

Outline:
classes
    noun
    verb
    grammar
        grunt work
        what structures are allowed
        how can parts of speech blend together
    generator
        productive, no rules

files
    main
        generate one or multiple sentences
        create instance of the generator
            uses grammar class
            has dictionary of nouns, verbs, etc.
        