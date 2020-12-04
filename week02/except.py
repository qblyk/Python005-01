import Exception

gennumber = (i for i in range(0,2))
print(next(gennumber))
print(next(gennumber))

try:
    print(next(gennumber))

except StopIteration:
    print('最后一个元素')