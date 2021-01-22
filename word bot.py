from PyDictionary import PyDictionary
dictionary=PyDictionary()
import nltk
from nltk.corpus import wordnet
synonyms = []
antonyms = []
print("Hi,I am a word bot.\n i can suport following commands\n1.hello\n2.bye\n3.meaning <words>\n4.synonmy <words>\n5.antonym <words>")
print("you can start")
options=input()
word=options[options.find('<')+len('<'):options.find('>')]
if(options.find("meanings")!=-1):
    print(dictionary.meaning(word))

elif(options.find("synonmy")!=-1):
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    print(set(synonyms))

elif(options.find("antonym")!=-1):
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    print(set(antonyms))
elif(options=='hello'):
    print('hello,happy to see you')
else:
    print('bye,Meet u soon\nmiss you')