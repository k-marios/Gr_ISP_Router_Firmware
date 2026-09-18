#!/usr/bin/env python3
import hashlib
import os
import sys
from Crypto.Cipher import AES

PERM_TABLE = "26aejsw37bfktx48chmuy59dipvz"
STR_1 = "b7293e8150d1330c6c3d93f2fa81331b"
STR_2 = "83f323b7132703029da5f4a9daa72a60"

def derive_key(version_str, seed_bytes):
    m1 = hashlib.md5()
    m1.update(version_str.encode("utf-8") + seed_bytes)
    h1 = m1.hexdigest()

    m2 = hashlib.md5()
    m2.update(h1.encode("utf-8") + STR_1.encode("utf-8"))
    h2 = m2.hexdigest()

    m3 = hashlib.md5()
    m3.update(h2.encode("utf-8") + STR_2.encode("utf-8"))
    raw_hash = m3.digest()

    derived_key = bytearray()
    for b in raw_hash:
        hex_str = f"{b:02x}"
        for hb in hex_str.encode("utf-8"):
            idx = hb % 28
            derived_key.append(ord(PERM_TABLE[idx % len(PERM_TABLE)]))

    return bytes(derived_key[:32])

def pad_data(data):
    block_size = AES.block_size
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)

def encrypt_firmware(input_ubi_path, output_img_path, version="1.2.02.08"):
    if not os.path.exists(input_ubi_path):
        print(f"[-] Error: {input_ubi_path} not found!")
        sys.exit(1)

    print(f"[*] Reading: {input_ubi_path}")
    with open(input_ubi_path, "rb") as f:
        payload = f.read()

    iv = os.urandom(16)
    seed = b"\x00" * 32

    print("[*] Deriving AES-256 key...")
    key = derive_key(version, seed)

    print("[*] Encrypting payload with AES-256-CBC...")
    padded_payload = pad_data(payload)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_payload = cipher.encrypt(padded_payload)

    # Construct Sercomm Header (160 bytes / 0xA0 offset)
    header = bytearray(160)
    header[0:8] = b"\x00\x00\x00\x00CS9\x00"

    v_bytes = version.encode("utf-8")
    header[0x20 : 0x20 + len(v_bytes)] = v_bytes
    header[0x40:0x50] = iv
    header[0x60:0x80] = seed

    payload_size_str = f"{len(encrypted_payload)}\x00".encode("ascii")
    header[0x80 : 0x80 + len(payload_size_str)] = payload_size_str

    print(f"[*] Writing encrypted image to: {output_img_path}")
    with open(output_img_path, "wb") as f:
        f.write(header)
        f.write(encrypted_payload)

    print(f"[+] Completed! Output image ready: {output_img_path}")

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "new_firmware.ubi"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "Vodafone_H300s_custom.img"
    encrypt_firmware(input_file, output_file)
