from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Define key, flag, and IV
key = bytes.fromhex('1615742b2a2930111211780908680016')
flag = "WRECKIT50{d0_y0u_th1nk_BFS_g0nna_s0lve_it?}"
iv = base64.b64decode("mJKl/x5xJ1viL34VEVDI7g==")

# Encryption
cipher = AES.new(key, AES.MODE_CBC, iv)
padded_flag = pad(flag.encode(), AES.block_size)
ciphertext = cipher.encrypt(padded_flag)

# Encode the ciphertext in base64
ciphertext_base64 = base64.b64encode(ciphertext).decode('utf-8')

# Decryption
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(base64.b64decode(ciphertext_base64)), AES.block_size)

print(f"Encrypted flag (base64): {ciphertext_base64}")
print(f"Decrypted flag: {decrypted.decode('utf-8')}")
