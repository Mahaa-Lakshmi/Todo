def process(word,options):
    from PyDictionary import PyDictionary
    dictionary=PyDictionary()
    import nltk
    from nltk.corpus import wordnet
    synonyms = []
    antonyms = []
    if(options==1):
        return (dictionary.meaning(word))

    elif(options==2):
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
        return(set(synonyms))

    elif(options==3):
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        return (set(antonyms))
