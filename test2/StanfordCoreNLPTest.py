from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'C:/gongyf/python/test2/', lang='zh')
sentence = '香港理工大学校长滕锦光表示，任何情况下暴力都不是解决问题的方法。'
print(nlp.ner(sentence))