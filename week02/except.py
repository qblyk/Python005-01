
gennumber = (i for i in range(0,2))
print(next(gennumber))
print(next(gennumber))

try:
    print(next(gennumber))

except StopIteration:
    print('最后一个元素')

try:
    a=1/0
    print(a)
except Exception as e:
    try:
        1/0
    except Exception as f:
        print('忽略异常')
        pass
    print(e)