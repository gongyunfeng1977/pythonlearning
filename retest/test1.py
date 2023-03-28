import re
phone_nmuber_regex = re.compile(f"\d\d\d-\d\d\d-\d\d\d\d") # 返回一个regex的模式对象，\d表示一个数字字符
mo = phone_nmuber_regex.search('My number is 425-455-4290.') # search() 查找传入的字符串，如果没有匹配到，就会返回None，匹配到了就会返回一个Match对象，Match对象有一个group()用法，他返回被查找字符串中实际匹配的文本(还是一个字符串)
print('Phone number found:'+mo.group()) # Phone number found:425-455-4290