# Vodafone H300s (Sercomm) Firmware Decryptor & Mod Tools

Reverse engineering, decryption, extraction, and modification tools for the **Vodafone H300s** (Sercomm) router firmware (tested on `v1.2.01.06_debug` and `v1.2.02.08`).

---

## 🛠️ Hardware & Architecture Overview
* **Processor:** Realtek RTL8685SB (MIPS interAptiv, multi-core)
* **Flash Type:** 16MB SPI-NAND Flash
* **File Systems:** 
  * Read-Only Rootfs: SquashFS over UBI (`mtd:ubi_vol_rootfs`)
  * Writable Persistent Storage: YAFFS2 (`/config`, `/mnt/appdat`, `/mnt/appdeb`)

---

## 🔐 Cryptography & Firmware Structure

Sercomm firmware images for this model use a custom header structure combined with **AES-256-CBC** encryption.

1. **Header Layout (First 160 Bytes / 0xA0 Offset):**
   * `0x00 - 0x08`: Magic bytes (e.g., `CS9` header `0000000043533900`)
   * `0x20 - 0x40`: Firmware version string (null-padded)
   * `0x40 - 0x50`: AES-CBC Initialization Vector (IV)
   * `0x60 - 0x80`: Seed bytes
   * `0x80 - 0x90`: ASCII string representing the expected payload length

2. **Key Derivation Pipeline:**
   The decryption key is derived using a 3-stage parallel MD5 hashing pipeline combined with a custom 28-character permutation table (`PERM_TABLE = "26aejsw37bfktx48chmuy59dipvz"`), transforming the intermediate hashes into a final 32-byte AES-256 key.

---

## 📜 Scripts Included

* **`decrypt_h300s.py`**: Automatically parses the Sercomm header, derives the AES-256 key using the version string and seed, decrypts the payload, and verifies the inner `UBI#` container.
* **`encrypt_h300s.py`**: Takes a modified UBI/SquashFS image, pads it via PKCS#7, encrypts it back with AES-256-CBC, and constructs a valid Sercomm `.img` container ready for flashing.
* **`test_h300s.py`**: Validates end-to-end encryption/decryption integrity by comparing SHA-256 hashes of the original and reconstructed images.

---

## 🚀 Usage

### 1. Decrypting Firmware
```bash
python decrypt_h300s.py Vodafone_H_300s_v1.2.02.08.img

```

### 2. Extracting UBI & SquashFS Rootfs

After obtaining the decrypted `.ubi` container (stripping the initial 288-byte Sercomm inner header):

```bash
# Strip the 288-byte inner header
dd if=Vodafone_H_300s_v1.2.02.08_decrypted.ubi of=pure.ubi bs=288 skip=1

# Extract UBI images using ubi_reader
ubireader_extract_images pure.ubi -o extracted

# Unpack SquashFS rootfs
unsquashfs -d rootfs_extracted extracted/*vol-ubi_vol_rootfs.ubifs

```

---

## ⚠️ Disclaimer

This repository is for educational, research, and self-hosted device auditing purposes only. Use these scripts at your own risk. Modifying router firmware incorrectly may result in a bricked device.
