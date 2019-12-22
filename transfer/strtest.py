import os
a = r"D:\PycharmProjects\deploy_python_01\datas\pic\0.jpg"
b = r"D:\PycharmProjects\deploy_python_01\datas\pic"
c = a[len(b):]
print(c)
d = "../datas"
e = os.path.abspath(d)
print(e)
f = b[len(e):]
print(f)
