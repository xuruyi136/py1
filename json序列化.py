import json
import pickle
# 将json类型的对象与json类型的字符串相互转换
# {} 与 [] 嵌套形成的数据（python中建议数据的从{}开始）
dic = {
    'a': 1,
    'b': [1, 2, 3, 4, 5]}
# 序列化: 将python的字典转化为字符串传递给其他语言或保存
json_str = pickle.dumps(dic)
print(json_str)
new_dic = pickle.loads(json_str)
print(new_dic)