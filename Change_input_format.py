# 把用户输入的名字(此处用预设的list代替)改成标准形式，即首字母大写其余小写
#Change the format of the input names by user
#Namely is capitalize the first letter and set the rest lowercase

input = ['LAwyer', 'DunkET', 'stool', 'fuckOFF']

def change_format(l):
    new = l[0].upper() + l[1:].lower()
    return new

output = map(change_format, input)
print output
