# Vodafone H300s (Sercomm) Firmware Toolkit

Complete tooling to decrypt, unpack, modify, rebuild, and re-encrypt firmware images for the **Vodafone H300s** (Sercomm) router. Verified on firmware releases `v1.2.01.06_debug` and `v1.2.02.08`.

---

## 🛠️ Hardware & Architecture Specifications

* **SoC:** Realtek RTL8685SB (MIPS interAptiv, multi-threading / 4 VPEs)
* **Flash:** 16MB SPI-NAND
* **Partitions:**
  * Rootfs: Read-only SquashFS 4.0 over UBI (`mtd:ubi_vol_rootfs`)
  * Persistent Storage: YAFFS2 (`/config` on `mtd9`, `/mnt/appdat` on `mtd10`, `/mnt/appdeb` on `mtd12`)

---

## 🔐 Firmware Encryption & Header Structure

Firmware images are encapsulated within a custom Sercomm container and encrypted using **AES-256-CBC**.

### 1. Outer Header Layout (First 160 Bytes / 0xA0)
* `0x00 - 0x08`: Magic signature (`\x00\x00\x00\x00CS9\x00` or zero-padded)
* `0x20 - 0x40`: Firmware version string (ASCII, null-padded)
* `0x40 - 0x50`: Initialization Vector (IV, 16 bytes)
* `0x60 - 0x80`: Seed bytes (32 bytes)
* `0x80 - 0x90`: Payload byte length (ASCII string, null-terminated)

### 2. Key Derivation Pipeline
The encryption key is generated via three parallel MD5 digests coupled with a 28-character permutation lookup table:

```

m1 = MD5(seed_60 + version)
m2 = MD5(STR_A + version)
m3 = MD5(STR_B + version)
d_final = MD5(m1 + m2 + m3)
key = [ TABLE[byte % 28] for byte in hex_format(d_final) ][:32]

```

### 3. Inner Container
Decrypting the payload yields an inner Sercomm container where the actual `UBI#` stream starts at offset **288** (`0x120`), organized in 128KB physical eraseblocks.

---

## 📦 Prerequisites & Dependencies

### System Packages
```bash
# Arch Linux
sudo pacman -S squashfs-tools mtd-utils python python-pip

# Debian / Ubuntu
sudo apt update && sudo apt install -y squashfs-tools mtd-utils python3 python3-pip

```

### Python Dependencies

```bash
pip install -r requirements.txt

```

---

## 🔧 Manual Workflow

### Step 1: Decrypt Firmware

```bash
python3 decrypt_h300s.py Vodafone_H_300s_v1.2.02.08.img

```

### Step 2: Strip Inner Header

```bash
dd if=Vodafone_H_300s_v1.2.02.08_decrypted.ubi of=pure.ubi bs=288 skip=1

```

### Step 3: Extract UBI Volumes

```bash
ubireader_extract_images pure.ubi -o extracted_ubi

```

### Step 4: Unpack Rootfs

```bash
unsquashfs -d rootfs_v1.2.02.08 extracted_ubi/*/*vol-ubi_vol_rootfs.ubifs

```

### Step 5: Re-encrypt Modified Image

```bash
python3 encrypt_h300s.py new_firmware.ubi Vodafone_H300s_custom.img

```

---

## ⚠️ Disclaimer

This project is intended strictly for personal research, educational purposes, and hardware auditing. Modifying firmware involves potential risks of bricking hardware.
