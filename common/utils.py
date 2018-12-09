def md5(info):
    import hashlib
    # import time
    # ctime = str(time.time())
    m = hashlib.md5(bytes(info, encoding='utf-8'))
    # m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

