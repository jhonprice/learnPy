#转义字符
tabby_cat="\tI'm tabbed in."
persian_cat="I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."



fat_cat = """
I'll do a list:
\t* Cat food
\t* Finishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)



#\Uxxxxxxxx (32位十六进制数)
#\uxxxx (16位十六进制数)
#\ooo 八进制
#\xhh 十六进制
