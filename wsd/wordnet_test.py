from nltk.corpus import wordnet as wn

# 展示同义词集
synsets1 = wn.synsets('bank')
print(synsets1)
# 带有词性的同义词集
synsets2 = wn.synsets('bank', pos=wn.VERB)
print(synsets2)

# 定义
print(wn.synset('bank.n.01').definition())
print(synsets1[0].definition())

# 例句
print(len(wn.synset('bank.n.01').examples()))
print(wn.synset('bank.n.01').examples()[0])

# lemmas
print(wn.synset('dog.n.01').lemmas())
print([str(lemma.name()) for lemma in wn.synset('dog.n.01').lemmas()])
print(wn.lemma('dog.n.01.dog').synset())
