OK = 20000  # 成功
ERROR = 20001  # 失败
LOGINERROR = 20002  # 用户名或密码错误
ACCESSERROR = 20003  # 权限不足
REMOTERROR = 20004  # 远程调用失败
REPERROR = 20005  # 重复操作

class StatusCode(object):
    @classmethod
    def OK(self):
        res = {}
        res['code'] = OK
        res['msg'] = '操作成功'
        return res

    @classmethod
    def ERROR(self):
        res = {}
        res['code'] = ERROR
        res['msg'] = '操作失败'
        return res

    @classmethod
    def ACCESSERROR(self):
        res = {}
        res['code'] = ACCESSERROR
        res['msg'] = '权限不足'
        return res

    @classmethod
    def LOGINERROR(self):
        res = {}
        res['code'] = LOGINERROR
        res['msg'] = '用户名或密码错误'
        return res

    @classmethod
    def REMOTERROR(self):
        res = {}
        res['code'] = REMOTERROR
        res['msg'] = '远程调用失败'
        return res

    @classmethod
    def REPERROR(self):
        res = {}
        res['code'] = REPERROR
        res['msg'] = '重复操作'
        return res