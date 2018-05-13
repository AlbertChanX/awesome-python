# pycryptodome
# Symmetric Cryptography
from Crypto.Cipher import AES
# 秘钥,此处需要将字符串转为字节
key = b'love '


class MyAESCrypto(object):
    """docstring for MyAESCrypto"""

    def __init__(self, key, mode=AES.MODE_ECB):
        self.key = self.pad(key)
        self.mode = mode

    def pad(self, text):
        """
        key or text -->*16, with b'\0'
        """
        while len(text) % 16 != 0:
            text += b'\0'
        return text

    def encrypt(self, text):
        # 进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
        aes = AES.new(self.key, self.mode)
        # 进行内容拼接16位字符后传入加密类中，结果为字节类型
        encrypted_text = aes.encrypt(self.pad(text))
        return encrypted_text

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode)
        plain_text = cryptor.decrypt(text)
        return plain_text.rstrip(b'\0').decode()


if __name__ == '__main__':
    text = b'i love u'
    c = MyAESCrypto(key)
    en_text = c.encrypt(text)
    de_text = c.decrypt(en_text)
    print(de_text)
