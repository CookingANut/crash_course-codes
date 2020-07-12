def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
    else:
    #计算文件大致包含多少个单词
        words = contents.split()
        numwords = len(words)
        print("The file " + filename + " has about " + str(numwords) + " words.")


filenames = [
    r'chapter10\alice.txt',
    r'chapter10\moby_dick.txt',
    r'chapter10\siddhartha.txt',
    r'chapter10\little_women.txt'
]

for filename in filenames:
     count_words(filename)


