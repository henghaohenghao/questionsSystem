#获取人物(角色)

import codecs

def get_character():
    f = codecs.open('../raw_data/三国演义关系.txt','r','utf-8')
    data = []
    for line in f.readlines():
        #strip用于移除字符串头尾指定的字符或字符序列,默认为空格
        array = line.strip("\n").split(",")
        arr = [array[0],array[1]]
        #extend将传入的对象参数中的元素序列追加到列表末尾
        data.extend(arr)

    return data