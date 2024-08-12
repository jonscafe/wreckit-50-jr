import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Define the key, flag, and IV
key = b'1615742b2a2930111211780908680016'
flag = "WRECKIT50{d0_y0u_th1nk_BFS_g0nna_s0lve_it?}"
iv = base64.b64decode("mJKl/x5xJ1viL34VEVDI7g==")

# Create a new AES cipher object with the key and IV in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad the flag to make its length a multiple of AES block size
padded_flag = pad(flag.encode(), AES.block_size)

# Encrypt the padded flag
ciphertext = cipher.encrypt(padded_flag)

# Encode the ciphertext in base64 for display
ciphertext_base64 = base64.b64encode(ciphertext).decode('utf-8')

print(f"Encrypted flag (ciphertext): {ciphertext_base64}")
