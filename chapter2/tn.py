#\t 制表符， \n换行符
print("Python")
print("\tPython")
print("Language:\n\tPython\n\tC\n\tJavaScript")

favorite_language="Python " 
favorite_language.rstrip()
print(favorite_language)
favorite_language=favorite_language.rstrip()

favorite_language=" Python "
favorite_language.rstrip()  #去除末尾的空白
favorite_language.strip()   #去除两端的空白
favorite_language.lstrip()  #去除开头的空白
print(favorite_language)
