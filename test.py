import re

str = '时尚街拍婚纱照：怎么街拍婚纱照好看?街拍婚纱照要注意什么?'
pattern = "[`~!@#$%^&*()_\-+=<>?:{}|,.\/;'\\[\]·~！@#￥%……&*（）——\-+={}|《》？：“”【】、；‘’，。、]"
title = re.sub(pattern=pattern, repl=' ', string=str)
print(title)