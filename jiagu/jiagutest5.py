import jiagu

fin = open('d:/gongyf/python/jiagu/input.txt', 'r')
text = fin.read()
fin.close()

summarize = jiagu.summarize(text, 3) # 摘要
print(summarize)