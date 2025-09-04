import time
import uuid

def generate_timestamp():
    """生成一个时间戳"""
    return int(time.time() * 1000)

def generate_nonce_str():
    """生成一个随机的 Nonce 字符串"""
    return str(uuid.uuid4()).replace('-', '')

class BuyBtcRequestBodyBase:
    """
    Python 版 BuyBtcRequestBodyBase 类
    """
    def __init__(self):
        self.request_time = str(generate_timestamp())
        self.nonce = generate_nonce_str()
        self.version = "v2.0"

    @staticmethod
    def attach(data: dict, force=False):
        """
        将基础字段附加到给定的数据对象上
        """
        if data is None:
            return data

        base = BuyBtcRequestBodyBase()

        # 检查 data 对象是否具有相应的属性
        if force or hasattr(data, 'requestTime'):
            data['requestTime'] = base.request_time
        
        if force or hasattr(data, 'nonce'):
            data['nonce'] = base.nonce

        if force or hasattr(data, 'version'):
            data['version'] = base.version

        return data