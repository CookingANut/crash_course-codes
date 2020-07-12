glossary = {
    '.rstrip()': '去除字符串末尾的空白。',
    '.rstrip()': '去除字符串开头的空白。',
    '.srip()': '去除字符串两边的空白。',
    '.title()': '以首字母大写的方式显示每个单词。',
    '.upper()': "将字符串全部改为大写。",
    '.lower()': "将字符串全部改成小写。",
    '.pop()' : "删除列表中末尾的元素。",
    '.sort()' :  "按照字母顺序排列列表，永久。",
    'reverse()': "反转列表元素的排列顺序。"
    }

#word = '.rstrip()'
#print("\n" + word.title() + ": " + glossary[word])
#word = '.rstrip()'
#print("\n" + word.title() + ": " + glossary[word])
#word = '.srip()'
#print("\n" + word.title() + ": " + glossary[word])
#word = '.title()'
#print("\n" + word.title() + ": " + glossary[word])
#word = '.upper()'
#print("\n" + word.title() + ": " + glossary[word])
#word = '.lower()'
#print("\n" + word.title() + ": " + glossary[word])

for item, meaning in glossary.items():
    print("\n" + item + ": " + meaning + ".")
