#!/usr/bin/env python3
import hashlib
import os
import sys
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

TABLE = b"26aejsw37bfktx48chmuy59dipvz"
STR_A = b"b7293e8150d1330c6c3d93f2fa81331b"
STR_B = b"83f323b7132703029da5f4a9daa72a60"

def decrypt_image(target_file):
    if not os.path.exists(target_file):
        print(f"[-] Error: {target_file} not found!")
        sys.exit(1)

    print(f"[*] Analyzing: {target_file}")
    with open(target_file, "rb") as f:
        img = f.read()

    version = img[0x20:0x40].split(b"\x00")[0]
    seed_60 = img[0x60:0x80]
    iv = img[0x40:0x50]
    payload = img[0xA0:]

    len_str = img[0x80:0x90].split(b"\x00")[0].decode(errors="ignore")
    expected_len = int(len_str)

    print(f"    - Header Version : {version.decode(errors='ignore')}")
    print(f"    - IV             : {iv.hex()}")
    print(f"    - Expected Size  : {expected_len} bytes")

    # 3-stage parallel MD5 key derivation
    m1 = hashlib.md5(seed_60 + version).digest()
    m2 = hashlib.md5(STR_A + version).digest()
    m3 = hashlib.md5(STR_B + version).digest()
    d_final = hashlib.md5(m1 + m2 + m3).digest()

    # C sprintf("%x") formatting simulation
    buf = bytearray(33)
    for i, b in enumerate(d_final):
        s = f"{b:x}".encode("ascii")
        buf[i * 2 : i * 2 + len(s)] = s
        buf[i * 2 + len(s)] = 0

    key = bytes([TABLE[c % 28] for c in buf[:32]])
    print(f"[+] Derived AES-256 Key: {key.decode('ascii')}")

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(payload[:expected_len]) + decryptor.finalize()

    if decrypted_data.startswith(b"UBI#"):
        print("[+] SUCCESS: Valid UBI magic found ('UBI#')!")
    else:
        print(f"[*] Inner header prefix: {decrypted_data[:8]}")

    out_name = os.path.splitext(target_file)[0] + "_decrypted.ubi"
    with open(out_name, "wb") as out_f:
        out_f.write(decrypted_data)

    print(f"[+] Decrypted image written: {out_name} ({len(decrypted_data)} bytes)")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "Vodafone_H_300s_v1.2.02.08.img"
    decrypt_image(target)
