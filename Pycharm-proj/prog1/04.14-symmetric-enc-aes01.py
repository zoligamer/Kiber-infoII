#AES symmetric

from Crypto.Cipher import AES
from Crypto.Random import random,get_random_bytes
from Crypto.Util.Padding import pad,unpad




key=get_random_bytes(16)
text="Niggaballs"
data=text.encode()

iv=get_random_bytes(16)

cipher=AES.new(key,AES.MODE_CBC,iv)
ciphertext=cipher.encrypt(pad(data,AES.block_size))
print(ciphertext.hex())

cipher=AES.new(key,AES.MODE_CBC,iv)
decoded=unpad(cipher.decrypt(ciphertext),AES.block_size)
print(decoded)
