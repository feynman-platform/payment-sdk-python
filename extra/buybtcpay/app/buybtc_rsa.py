from typing import cast
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
import base64

def normalize_dict_to_content(data_dict: dict) -> str:
    """
    将字典按key排序并转换成 key1=value1&key2=value2 格式的字符串。
    支持嵌套字典。

    Args:
        data_dict (dict): 待处理的字典。

    Returns:
        str: 格式化后的字符串。
    """
    # 递归函数，处理嵌套字典和列表
    def _to_content(obj):
        if isinstance(obj, dict):
            # 将字典按key排序
            sorted_items = sorted(obj.items())
            
            # 递归处理每个值
            parts = [f"{key}={_to_content(value)}" for key, value in sorted_items if value is not None]
            
            return "&".join(parts)
        elif isinstance(obj, list):
            # 递归处理列表中的每个元素
            parts = [f"{_to_content(item)}" for item in obj if item is not None]
            
            return "[" + ",".join(parts) + "]"
        else:
            # 基础类型直接转换为字符串
            return str(obj)

    # 如果顶层是字典，直接调用递归函数
    if isinstance(data_dict, dict):
        return _to_content(data_dict)
    else:
        return _to_content({})

def compose_public_key_pem(public_key_base64: str) -> bytes:
    """
    将纯Base64编码的密钥字符串重新组装为标准的PEM格式。
    """
    # 确定PEM格式的头和尾
    header = "-----BEGIN PUBLIC KEY-----"
    footer = "-----END PUBLIC KEY-----"

    # 将Base64字符串分割成每行64个字符
    # 这一步不是严格必需的，但符合PEM标准，能提高兼容性
    formatted_key = '\n'.join(public_key_base64[i:i + 64] for i in range(0, len(public_key_base64), 64))

    # 组装完整的PEM字符串
    pem_string = f"{header}\n{formatted_key}\n{footer}"
    
    return pem_string.encode('utf-8')

def compose_private_key_pem(private_key_base64: str) -> bytes:
    """
    将纯Base64编码的密钥字符串重新组装为标准的PEM格式。
    """
    # 确定PEM格式的头和尾
    header = "-----BEGIN PRIVATE KEY-----"
    footer = "-----END PRIVATE KEY-----"

    # 将Base64字符串分割成每行64个字符
    # 这一步不是严格必需的，但符合PEM标准，能提高兼容性
    formatted_key = '\n'.join(private_key_base64[i:i + 64] for i in range(0, len(private_key_base64), 64))

    # 组装完整的PEM字符串
    pem_string = f"{header}\n{formatted_key}\n{footer}"
    
    return pem_string.encode('utf-8')



def sign_with_rsa(message: str, private_key_base64: str) -> str:
    """
    使用Base64编码的RSA私钥对消息进行签名。
    私钥格式为 PKCS8。

    Args:
        message (str): 待签名的消息字符串。
        private_key_base64 (str): Base64编码的RSA私钥字符串。

    Returns:
        str: Base64编码的签名结果字符串。
    """
    # 1. 将Base64密钥字符串解码为字节串
    private_key_pem = compose_private_key_pem(private_key_base64)
    
    # 2. 加载私钥 (PKCS8 格式)
    private_key: RSAPrivateKey = cast(RSAPrivateKey, serialization.load_pem_private_key(
        private_key_pem,
        password=None,  # 如果私钥有密码，请在这里提供
    ))
    
    # 3. 签名：使用 PSS 填充模式和 SHA256 哈希算法
    signature = private_key.sign(
        message.encode('utf-8'),
        padding.PKCS1v15(),
        # padding.PSS(
        #     mgf=padding.MGF1(hashes.SHA256()),
        #     salt_length=padding.PSS.MAX_LENGTH
        # ),
        hashes.SHA256()
    )
    
    return base64.b64encode(signature).decode('utf-8')

def verify_with_rsa(message: str, signature: str, public_key_base64: str) -> bool:
    """
    使用Base64编码的RSA公钥验证签名。
    公钥格式为 X.509。

    Args:
        message (str): 原始消息字符串。
        signature (str): Base64编码的签名字符串。
        public_key_base64 (str): Base64编码的RSA公钥字符串。

    Returns:
        bool: 如果签名正确返回 True，否则返回 False。
    """
    try:
        # 1. 将Base64公钥字符串解码为字节串
        public_key_pem = compose_public_key_pem(public_key_base64)

        # 2. 加载公钥 (X.509 格式)
        public_key: RSAPublicKey = cast(RSAPublicKey, serialization.load_pem_public_key(
            public_key_pem,
        ))

        # 3. 解码签名并验证
        decoded_signature = base64.b64decode(signature)

        public_key.verify(
            decoded_signature,
            message.encode('utf-8'),
            padding.PKCS1v15(),
            # padding.PSS(
            #     mgf=padding.MGF1(hashes.SHA256()),
            #     salt_length=padding.PSS.MAX_LENGTH
            # ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"验证失败: {e}")
        return False

# --- 示例和自检 ---

if __name__ == '__main__':
    # 假设你已经有了Base64编码的私钥和公钥
    # 这里的密钥是示例，请替换为你的实际密钥
    # 建议使用 https://www.devglan.com/online-tools/rsa-key-generator
    # 或类似工具生成 PKCS8 私钥和 X.509 公钥
    PrivateKey = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCzr6Fn2BcCFCFKDH0k9bY3FEpRhVyTGO+GMPgHLaObMET3xPM19JPlHJSkGgbulJaJAutgIYnAKqmFi2m6z82MwcLT60gZ/f4tQcfDN9PfOlBFKcpVE/gDvZPUJS5qHfauzxhjNnbIh7zjtpmcImelljDbi+b7s18CX9sm3JMbu1jmgbuexx3+4fhhrtG0sx0CV3rc/OtOJox1OvSyuzhQi3w86KCTbwqVHMbHfM+X4/EZQghoCQPjrboqyNR7SKOth655OPevwDkBOPW95Piyt1kCx/9k2ruFz86A3owNx2TMvBX5Acr/rDitDpVmMVoUa460RmwDj7mo4vmq5xHNAgMBAAECggEAKBZ6qtWPuoe9rozPPbfw7WRiOUJI10uEorpZl5Zjzhtsg5+lyCeW+FJSSjNBUSiG1i33z9RjrGMIO5JRJhu25tySqB9xkFT1iGjI1cGmjAKxRmDusmD4X/NDYBzkeEnTj4gGD5pm0VHRPzdtmWMmnw99OnoBsC2COKAkn0yuKE0YtloYczMTVMc3DZy2U9jXpuaVv3NRi2y5rBgKvNKDXrm2Tvkj9SLH4cuh/onHpM/Z0FLMIK3PKdMCbTn67h4gvmOAeSYyvTRHmKGGragpVig1OxUIVkh+GU7Ys7sBSC/wvg3dlbL/zfUCdgGrvg86366lOPqFB1DuiqV+Tf9w2QKBgQD71oxN2EV+MBPsGOysbaTgcX36xQPfjeANzF90wdUJhER7wFHFSxqQiwkRBZP2KeHLi7WaaNfVxU2dWsf1HMao+C0lfeSUPSLVzhqLuZvrXhDR18afTQEg529YyI0HkzT47i2aYHp/AYJjfZCk8BJTxxF9VfvgQwi0jy8ogmWjVQKBgQC2p9Ql6y2Rim6uQsQHY5nFzvHVvvLIQCMbnH8yTz2ggAQ5DwHYVzH0GJLw68OLMdA3329iLKnZU2Sw6j3ufZtNximCMudhgGcR7y/h6L8zibgCEe6+OlYlWBWeU2qKq02/tK62yHYulU+hmH1cjVaaXLcmhWfpkACpAMB2rW6kmQKBgQCl6Wr1vg3KXJJDcQg7cOC2nQ6KL1Gl7io17PbWTPy1EFat0L4OZLRTlcWbWTlpa54+IwS5fWj0hM/lYvFpIlQe7aGQmagFoWFZyjbi5p06KvaZyLYqLOkZbF+G9lkzLGAxv3h7xCPvmGb2dLrebuskFnoHQKZ30LHjgpFm9sFPIQKBgH0bvULvr/mlQSRZFN4eyZ/knF6UeMTSsXljGviBsCt0I/BVKCVfrBaOkm80fW6lAwKSJz+uafQym6BWAW+OV0bROXM1nKh7A54UH87z1areZMv+LnHbkU/o4n3ckvhCV3G8t4L5EYHcwXtk8FDpem0mnkhjTgZ7nQglPK7NIiDZAoGBAI2tcYOJg0/FJmm40n/k38LjH+H+qEdFeq8bCUJA6oVjW1jowiHqXE8L23t5cM5pMn1YfU6wUfqa6eEnPuPCOa63nPd/I61JaIEsSc0KV7bla1x9J9xHFr2OF2YLp/sWNOIHevdT4ZlNeosUbtsAw/35IK079VEhoWIzTtaQfQPp"
    PublicKey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs6+hZ9gXAhQhSgx9JPW2NxRKUYVckxjvhjD4By2jmzBE98TzNfST5RyUpBoG7pSWiQLrYCGJwCqphYtpus/NjMHC0+tIGf3+LUHHwzfT3zpQRSnKVRP4A72T1CUuah32rs8YYzZ2yIe847aZnCJnpZYw24vm+7NfAl/bJtyTG7tY5oG7nscd/uH4Ya7RtLMdAld63PzrTiaMdTr0srs4UIt8POigk28KlRzGx3zPl+PxGUIIaAkD4626KsjUe0ijrYeueTj3r8A5ATj1veT4srdZAsf/ZNq7hc/OgN6MDcdkzLwV+QHK/6w4rQ6VZjFaFGuOtEZsA4+5qOL5qucRzQIDAQAB";
    BuyBtcPublickKey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn3LGfzlKDrsJlJoWN7+lPJMAEF64IKuhPDkZS0LpgyWdqhJewvomD+AWQEdhNAGh0yESKV28L+HjxQSKz1GnHxP/MhZEK5UyB/Hvgi/vLAZ4/f3m6QGowqog5yPDm2a4vL5d67mPajFNKgEF5arGyj+bIsnSof2iuc7KpibbKtmRsayz2Y23WmAZta1Jt/SnoniHw9jFVG3IoDL6P9NaK+u0W4eURFKARRpcDSFPJ9juDOa1d34Tru7LX25x0eKqPnGUrtxqG0adoHprQjKPYjy+6ShEqvMaB92jUgYWRNpxmsZJ/5t0eOzZ3x/9Lpt9N2Y6L0Y/lBpPhG8cLpGxYQIDAQAB";

    
    base64_private_key_str = PrivateKey
    base64_public_key_str = PublicKey
    
    original_message = "这是一条用于测试签名的消息。"
    print(f"原始消息: '{original_message}'")
    
    # 进行签名
    print("\n进行签名...")
    signature = sign_with_rsa(original_message, base64_private_key_str)
    print(f"签名 (Base64): {signature}")
    
    # 进行验签
    print("\n进行验签...")
    is_valid = verify_with_rsa(original_message, signature, base64_public_key_str)
    print(f"签名是否有效? {is_valid}")
    
    # 测试失败场景：篡改消息
    tampered_message = "这条消息被篡改了。"
    print("\n测试篡改后的消息...")
    is_tampered_valid = verify_with_rsa(tampered_message, signature, base64_public_key_str)
    print(f"篡改后签名是否有效? {is_tampered_valid}")
