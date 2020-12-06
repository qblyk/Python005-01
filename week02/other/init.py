class UserInputError(Exception):
    def __init__(self,ErrorInfo):  #__*__初始化时即执行的类
        super().__init__(self,ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo
userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    del userinput