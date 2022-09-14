# 输入的变量为int类型， 还回的是str 都是注释
def func(m:int) -> str:
    print(type(m))
    print(m)

func('s')