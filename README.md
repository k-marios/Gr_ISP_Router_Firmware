# Greek ISP Router Firmware Archive

[![Status](https://img.shields.io/badge/Status-Preservation%20Archive-blue.svg)](#)
[![Region](https://img.shields.io/badge/Region-Greece%20%F0%9F%87%AC%F0%9F%87%B7-1e88e5.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](#contributing)

<br/>

[![Cosmote](https://img.shields.io/badge/Cosmote-008A00?style=flat&logoColor=white)](Cosmote/)
[![Cyta](https://img.shields.io/badge/Cyta-792482?style=flat&logoColor=white)](Cyta/)
[![Forthnet](https://img.shields.io/badge/Forthnet-F58220?style=flat&logoColor=white)](Forthnet/)
[![HOL](https://img.shields.io/badge/HOL-E30613?style=flat&logoColor=white)](HOL/)
[![Nova](https://img.shields.io/badge/Nova-000000?style=flat&logoColor=white)](Nova/)
[![OTE](https://img.shields.io/badge/OTE-00458C?style=flat&logoColor=white)](OTE/)
[![PPC](https://img.shields.io/badge/PPC-white?style=flat&logoColor=white)](PPC/)
[![Vodafone](https://img.shields.io/badge/Vodafone-E60000?style=flat&logo=vodafone&logoColor=white)](Vodafone/)
[![Wind](https://img.shields.io/badge/Wind-009FE3?style=flat&logoColor=white)](Wind/)


>A centralized, community-driven preservation repository archiving ISP-customized firmware binaries, recovery images, and documentation for CPE routers, VoIP gateways, and modems distributed by Greek Internet Service Providers (both active and legacy).

---

## ToC

- [Why This Repository Exists](#why-this-repository-exists)
- [Root Passwords & Superuser Guide](#root-passwords--superuser-guide)
- [Provider & Hardware Catalog](#provider--hardware-catalog)
  - [1. Cosmote](#1-cosmote)
  - [2. Cyta Hellas (Legacy)](#2-cyta-hellas-legacy)
  - [3. Forthnet (Legacy)](#3-forthnet-legacy)
  - [4. HOL - Hellas On-Line (Legacy)](#4-hol---hellas-on-line-legacy)
  - [5. Nova](#5-nova)
  - [6. OTE (Legacy)](#6-ote-legacy)
  - [7. PPC - Public Power Corporation](#7-ppc---public-power-corporation)
  - [8. Vodafone Greece](#8-vodafone-greece)
  - [9. Wind Hellas (Legacy)](#9-wind-hellas-legacy)
- [Critical Flashing & Operation Tips](#critical-flashing--operation-tips)
- [Repository Directory Structure](#repository-directory-structure)
- [Contributing](#contributing)
- [Legal Disclaimer & Copyright](#legal-disclaimer--copyright)

---

##  Why This Repository Exists

Greek Internet Service Providers deploy custom CPE (Customer Premises Equipment) with customized OEM firmware. Over time:

- **E-Waste Reduction:** Hundreds of thousands of functional CPE devices are abandoned or discarded as electronic waste once ISP contracts terminate. Having access to firmware empowers users to repair, unlock, and give these devices a second life—repurposing them for homelab projects, secondary subnets, standalone Wi-Fi APs, or managed switches.
- **Lost Official Firmware:** Official ISP download pages are often decommissioned or never made public in the first place.
- **De-bricking & Recovery:** When tweaking, experimenting with custom VoIP credentials, or recovering from a bad flash, having verified stock firmware images is critical.
- **Hardware Preservation:** Preserving firmware for historical hardware from legacy operators (HOL, Cyta, Forthnet, Wind) ensures vintage devices remain functional and documented for archival purposes.

---

## Root Passwords & Superuser Guide

Looking for root credentials, superuser logins, or hidden maintenance accounts for your Greek router?

**Check our comprehensive [ROOT_PASSWORDS.md](ROOT_PASSWORDS.md)** for detailed guides and credentials covering:
- **Vodafone:** Sercomm H300s (pre & post 1.2.01.06), ZTE H267A, ZTE H268Q (WiFi 5 & WiFi 6), TP-Link Archer VR100v.
- **Wind Hellas:** Technicolor TG788v v3, TG789vac v2, DGA 4130, ZTE H288A, Zyxel VMG8623-T50B.
- **Nova & Forthnet:** Older Technicolor & ZTE models, post-merger Nova/Wind firmware credentials (ZTE H288A, Nokia G-2425G-A, Huawei DG8245V-10).

---

## Provider & Hardware Catalog

The archive is organized hierarchically by `Provider / Manufacturer / Model`.

### 1. Cosmote
[![Cosmote](https://img.shields.io/badge/Cosmote-008A00?style=flat&logoColor=white)](Cosmote/)  
*Folder: [`Cosmote/`](Cosmote/)*

| Manufacturer | Model / Device Name | Technology / Type | Notes |
| :--- | :--- | :--- | :--- |
| **Arcadyan** | [Speedport Plus 2](Cosmote/Arcadyan/Speedport_Plus_2/) | VDSL2 / Vectoring / VoIP | ⚠️ *Do not cross-flash with Sercomm Plus 2* |
| **Huawei** | [HA35-10](Cosmote/Huawei/HA35-10/) | VDSL2 + 4G Hybrid Access | Cosmote Home SpeedBooster (Bonded DSL + LTE) |
| **Oxygen** | [HDI24201](Cosmote/Oxygen/HDI24201/), [HDI34201](Cosmote/Oxygen/HDI34201/) | VDSL2 / Multi-line VoIP / ISDN | Business PBX / Enterprise Gateways |
| **Sercomm** | [Speedport Plus 1](Cosmote/Sercomm/Speedport_Plus_1/) | VDSL2 35b / Vectoring / VoIP | - |
| **Sercomm** | [Speedport Plus 2](Cosmote/Sercomm/Speedport_Plus_2/) | VDSL2 / Vectoring / VoIP | ⚠️ *Do not cross-flash with Arcadyan Plus 2* |
| **Sercomm** | [Speedport W 724V (Type Ci)](Cosmote/Sercomm/Speedport_W_724V_Type_Ci/) | VDSL2 / VoIP | Legacy Gigabit dual-band CPE |
| **ZTE** | [Speedport Entry 2i](Cosmote/ZTE/Speedport_Entry_2i/) | VDSL2 17a / VoIP | Popular workhorse VDSL router |
| **ZTE** | [ZXHN H1600](Cosmote/ZTE/H1600/) | VDSL2 35b / Wi-Fi 6 / VoIP | Includes [Firmware Changelog](Cosmote/ZTE/H1600/README.md) |

---

### 2. Cyta Hellas (Legacy)
[![Cyta](https://img.shields.io/badge/Cyta-792482?style=flat&logoColor=white)](Cyta/) *(Acquired by Vodafone)*  
*Folder: [`Cyta/`](Cyta/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **ZTE** | [ZXHN H208N](Cyta/ZTE/H208N/) | Cyta VDSL2 / VoIP Gateway |
| **ZTE** | [ZXHN H267N](Cyta/ZTE/H267N/) | Cyta VDSL2 / VoIP Gateway |

---

### 3. Forthnet (Legacy)
[![Forthnet](https://img.shields.io/badge/Forthnet-F58220?style=flat&logoColor=white)](Forthnet/) *(Rebranded to Nova)*  
*Folder: [`Forthnet/`](Forthnet/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **AirTies** | [RT-111](Forthnet/Airties/RT-111/) | ADSL2+ / Fast Ethernet Router |
| **D-Link** | [DSL-2640B](Forthnet/D-Link/DSL-2640B/) | ADSL2+ / 802.11g Wireless Router |
| **Huawei** | [DG8245V-10](Forthnet/Huawei/DG8245V-10/) | VDSL2 / 802.11ac VoIP Gateway |
| **Huawei** | [HG521](Forthnet/Huawei/HG521/) | ADSL2+ / 802.11n Wireless Router |
| **Linksys** | [WAG200G](Forthnet/Linksys/WAG200G/), [WAG354G](Forthnet/Linksys/WAG354G/) | ADSL2+ / 802.11g Wireless Routers |
| **Siemens** | [CL110](Forthnet/Siemens/CL110/), [CL110i](Forthnet/Siemens/CL110i/) | ADSL2+ Modems / PSTN, ISDN respectively |
| **Technicolor** | [TD5130](Forthnet/Technicolor/TD5130/) | ADSL2+ / 802.11n Wireless Router |
| **Technicolor** | [TG788vn](Forthnet/Technicolor/TG788vn/), [TG788v v3](Forthnet/Technicolor/TG788v_v3/) | Classic Forthnet VDSL modems |
| **Thomson** | [TG585 v7](Forthnet/Thomson/TG585_v7/), [TG585 v8](Forthnet/Thomson/TG585_v8/) | ADSL2+ / 802.11g Wireless Routers |
| **US Robotics** | [USR9108](Forthnet/US_Robotics/USR9108/) | ADSL2+ / 802.11g Wireless Router |
| **US Robotics** | [USR9112](Forthnet/US_Robotics/USR9112/) | ADSL2+ Modem |
| **ZTE** | [ZXHN H108L](Forthnet/ZTE/H108L/) | ADSL2+ / 802.11n Router |
| **ZTE** | [ZXHN H108N v2.5](Forthnet/ZTE/H108N_v2.5/) | ADSL2+ router |
| **ZTE** | [ZXHN H288A](Forthnet/ZTE/H288A/) | VDSL2 35b / VoIP |

---

### 4. HOL - Hellas On-Line (Legacy)
[![HOL](https://img.shields.io/badge/HOL-E30613?style=flat&logoColor=white)](HOL/) *(Acquired by Vodafone)*  
*Folder: [`HOL/`](HOL/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **Alcatel-Lucent** | [CellPipe 7130](HOL/Alcatel/CellPipe_7130/) | Early VDSL2 / ADSL2+ gateway |
| **AVM (Fritz!)** | [Fritz!Box Fon WLAN 7140](HOL/Fritz/Box_7140/) | Annex A & Annex B German PBX router (HOL edition) |
| **Intracom** | [NetFasteR IAD](HOL/Intracom/Netfaster_IAD/) | Annex A & B VoIP gateway |
| **Intracom** | [NetFasteR IAD 2](HOL/Intracom/Netfaster_IAD2/), [IAD 3](HOL/Intracom/Netfaster_IAD3/) | Legendary Greek VoIP CPEs |
| **Intracom** | [NetFasteR IAD 3](HOL/Intracom/Netfaster_IAD3) | ADSL2+ VoIP gateway |
| **Technicolor** | [TD5136v2](HOL/Technicolor/TD5136v2/) | ADSL2+ router |
| **ZTE** | [ZXHN H108N v2.3](HOL/ZTE/H108N_v2.3/) | ADSL2+ gateway |
| **ZTE** | [ZXHN H168N](HOL/ZTE/H168N/) | VDSL2 gateway |

---

### 5. Nova
[![Nova](https://img.shields.io/badge/Nova-000000?style=flat&logoColor=white)](Nova/)  
*Folder: [`Nova/`](Nova/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **Huawei** | [DN8245V-70](Nova/Huawei/DN8245V-70/) | SuperVectoring 35b / Dual-Band Wi-Fi / VoIP Gateway |
| **ZTE** | [ZXHN H288A](Nova/ZTE/H288A/) | Gigabit VDSL2 35b / AC1600 / VoIP |
| **Zyxel** | [VMG1312-T20B](Nova/Zyxel/VMG1312-T20B/) | VDSL2 / Multi-WAN Router |
| **Zyxel** | [VMG8623-T50B](Nova/Zyxel/VMG8623-T50B/) | AC2400 Dual-Band VDSL2 / VoIP Gateway |

---

### 6. OTE (Legacy)
[![OTE](https://img.shields.io/badge/OTE-00458C?style=flat&logoColor=white)](OTE/)  
*Folder: [`OTE/`](OTE/)*

| Manufacturer | Model / Device Name | Technology / Type | Notes |
| :--- | :--- | :--- | :--- |
| **Intracom** | [JetSpeed 520](OTE/Intracom/Jetspeed_520/) | ADSL / ADSL2+ | Annex A & Annex B images |
| **ZTE** | [ZXDSL 931VII](OTE/ZTE/931VII/) | VDSL2 17a | One of the first VDSL CPEs to be given out by OTE |
| **ZTE** | [ZXHN H108NS](OTE/ZTE/H108NS/) | ADSL2+ | Annex A & Annex B variants |
| **ZTE** | [ZXV10 W300](OTE/ZTE/W300/) | ADSL2+ | Annex A & Annex B variants |

---

### 7. PPC - Public Power Corporation
[![PPC](https://img.shields.io/badge/PPC-white?style=flat&logoColor=white)](PPC/)  
*Folder: [`PPC/`](PPC/)*

| Manufacturer | Model / Device Name | Technology / Highlights |
| :--- | :--- | :--- |
| **ZTE** | [ZXHN F6625P](PPC/ZTE/F6625P/) | GPON / Wi-Fi 6 FTTH Gateway |
| **ZTE** | [ZXHN F8648P](PPC/ZTE/F8648P/) | XGS-PON / Wi-Fi 6 FTTH Gateway |
| **ZTE** | [ZXHN F8748](PPC/ZTE/F8748/) | XGS-PON / Wi-Fi 7 FTTH Gateway |

---

### 8. Vodafone Greece
[![Vodafone](https://img.shields.io/badge/Vodafone-E60000?style=flat&logo=vodafone&logoColor=white)](Vodafone/)  
*Folder: [`Vodafone/`](Vodafone/)*

Split into **Retail** (residential, often referred to as ODP) and **OneNet** (business/enterprise) solutions:

#### Retail Solutions (`Vodafone/Retail/`)
| Manufacturer | Model / Device Name | Technology / Highlights |
| :--- | :--- | :--- |
| **AirTies** | [Super Wi-Fi Extender](Vodafone/Retail/Airties/Super_WiFi_Extender/) | Wi-Fi 6 Mesh Extender (VDF4960) |
| **Huawei** | [H155-383](Vodafone/Retail/Huawei/H155-383/) | 5G NR / Wi-Fi 6 Gateway |
| **Sercomm** | [H300s](Vodafone/Retail/Sercomm/H300s/) | VDSL2 35b / VoIP / AC1600 |
| **Sercomm** | [Power Station Wi-Fi 6](Vodafone/Retail/Sercomm/Power_Station_WiFi6/) | VDSL2 35b / Wi-Fi 6 AX / VoIP |
| **TP-Link** | [Archer VR100v](Vodafone/Retail/TP-LINK/100V/) | VDSL2 / VoIP Gateway |
| **Vantiva** | [Ultra Hub 7](Vodafone/Retail/Vantiva/Ultra_Hub_7/) | Wi-Fi 7 / FTTH Gateway |
| **ZTE** | [ZXHN H108N (v2.5)](Vodafone/Retail/ZTE/H108N_v2.5/) | ADSL2+ |
| **ZTE** | [ZXHN H208N](Vodafone/Retail/ZTE/H208N/), [H267N](Vodafone/Retail/ZTE/H267N/) | VDSL2 / VoIP |
| **ZTE** | [ZXHN H267A](Vodafone/Retail/ZTE/H267A/) | VDSL2 17a / Dual-band AC / VoIP |
| **ZTE** | [ZXHN H268Q](Vodafone/Retail/ZTE/H268Q/), [H268Q Wi-Fi 6](Vodafone/Retail/ZTE/H268Q_WiFi6/) | VDSL2 35b / Wi-Fi 5 & Wi-Fi 6 / VoIP |
| **ZTE** | [ZXHN H367N](Vodafone/Retail/ZTE/H367N/) | VDSL2 / VoIP |
| **ZTE** | [MC888 Ultra](Vodafone/Retail/ZTE/MC888_Ultra/) | 5G R16 / Wi-Fi 6 CPE |
| **ZTE** | [MF289F](Vodafone/Retail/ZTE/MF289F/) | 4G+ / LTE Cat20 Gateway |

#### OneNet Business Solutions (`Vodafone/OneNet/`)
| Manufacturer | Models | Highlights |
| :--- | :--- | :--- |
| **Aethra** | BG8542(E)WAC/HWAX, BG8544(E)WAC, SV6044EM, XV8800 series | Enterprise VoIP & Multi-WAN business routers |
| **Nokia** | FastMile 5G Receiver HG-1 & HG-2 | Pro-grade 5G NR Outdoor Units |
| **OneAccess** | One100 Series | Enterprise-oriented multi-service access routers and VoIP IADs |
| **Oxygen** | EIA03002, HDV24201, HPV05200/05400/15400, IKA34200, IVL32100, IVV14200/34200, OIA35402/45402, OJA35800, OJV35800/55800, OLA42004/55204 | Carrier-grade IP PBX & ISDN/VoIP gateways |
| **Sercomm** | H300s (OneNet variant) | Business-configured Sercomm router |
| **ZTE** | H267A, H268Q (WiFi 5 & WiFi 6), MC888 Ultra OneNet editions | OneNet SIP trunking / voice firmware |

---

### 9. Wind Hellas (Legacy)
[![Wind](https://img.shields.io/badge/Wind-009FE3?style=flat&logoColor=white)](Wind/) *(Merged into Nova)*  
*Folder: [`Wind/`](Wind/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **Technicolor** | [DGA 4130](Wind/Technicolor/DGA4130/) | Broadcom-based VDSL2 35b gateway (Homeware / OpenWrt moddable) |
| **Technicolor** | [TG788v v3](Wind/Technicolor/TG788v_v3/) | VDSL2 Gateway |
| **Technicolor** | [TG789vac v2](Wind/Technicolor/TG789vac/) | Dual-band AC VDSL2 Gateway |
| **ZTE** | [ZXHN H108L](Wind/ZTE/ZXHN_H108L/), [ZXV10 H108L](Wind/ZTE/ZXV10_H108L/) | ADSL2+, 2 different variants |
| **ZTE** | [ZXHN H108N v2.5](Wind/ZTE/H108N_v2.5/) | ADSL2+ / 802.11n Gateway |
| **ZTE** | [ZXHN H168N](Wind/ZTE/H168N/) | VDSL2 17a / 802.11n Gateway |
| **ZTE** | [ZXHN H268N](Wind/ZTE/H268N/) | VDSL2 17a / 802.11n VoIP Gateway |
| **ZTE** | [ZXHN H288A](Wind/ZTE/H288A/) | VDSL2 35b / 802.11ac VoIP Gateway |
| **Zyxel** | [VMG1312-B10A](Wind/Zyxel/VMG1312-B10A/), [VMG1312-B10D](Wind/Zyxel/VMG1312-B10D/) | Legacy VDSL2 802.11n Gateways |
| **Zyxel** | [VMG8623-T50B](Wind/Zyxel/VMG8623-T50B/) | Dual-Band VDSL2 Gateway |

---

## ⚡ Critical Flashing & Operation Tips

> [!WARNING]
> **Prevent TR-069 Auto-Upgrade Right After Flashing!**
> Greek ISPs use Auto-Configuration Servers (ACS via TR-069/CWMP). When you downgrade or flash an older firmware, the router will automatically reconnect to the ACS once DSL or WAN sync is established and force-upgrade itself back to the latest locked firmware.
>
> **Recommended Step:** Keep the telephone/DSL line and WAN ethernet cable **DISCONNECTED** during and immediately after flashing. Log into the router locally, back up settings, obtain root / change passwords, and disable TR-069 or block the ACS domain before plugging the WAN/DSL cable back in.

> [!IMPORTANT]
> **Check Manufacturer Revisions (e.g. Speedport Plus 2):**
> Cosmote distributed the *Speedport Plus 2* using two completely different hardware platforms:
> - **Arcadyan** (`Cosmote/Arcadyan/Speedport_Plus_2/`)
> - **Sercomm** (`Cosmote/Sercomm/Speedport_Plus_2/`)
>
> Check the physical label on the bottom of the device before flashing. Attempting to flash an Arcadyan image onto a Sercomm board (or vice versa) will permanently brick the router.

> [!NOTE]
> **Annex A vs Annex B (PSTN vs ISDN):**
> Older ADSL/VDSL models (Intracom JetSpeed, Speedport Entry 2i, ZTE H108NS, Fritz!Box 7140) have separate firmware binaries depending on whether the line is Annex A (PSTN) or Annex B (ISDN). Flashing the incorrect annex will result in the modem being unable to sync with the DSLAM.

---

## 📂 Repository Directory Structure

```text
Gr_ISP_Router_Firmware/
├── Cosmote/
│   ├── Arcadyan/
│   ├── Huawei/
│   ├── Oxygen/
│   ├── Sercomm/
│   └── ZTE/
├── Cyta/
│   └── ZTE/
├── Forthnet/
│   ├── Airties/
│   ├── D-Link/
│   ├── Huawei/
│   ├── Linksys/
│   ├── Siemens/
│   ├── Technicolor/
│   ├── Thomson
│   ├── US_Robotics/
│   └── ZTE/
├── HOL/
│   ├── Alcatel/
│   ├── Fritz/
│   ├── Intracom/
│   ├── Technicolor/
│   └── ZTE/
├── Nova/
│   ├── Huawei/
│   ├── ZTE/
│   └── Zyxel/
├── OTE/
│   ├── Intracom/
│   └── ZTE/
├── PPC/
│   └── ZTE/
├── Vodafone/
│   ├── Retail/
│   │   ├── Airties/
│   │   ├── Huawei/
│   │   ├── Sercomm/
│   │   ├── TP-LINK/
│   │   ├── Vantiva/
│   │   └── ZTE/
│   └── OneNet/
│       ├── Aethra/
│       ├── Nokia/
│       ├── OneAccess/
│       ├── Oxygen/
│       ├── Sercomm/
│       └── ZTE/
├── Wind/
│   ├── Technicolor/
│   ├── ZTE/
│   └── Zyxel/
├── DISCLAIMER.md
├── DISCLAIMER_GR.md
├── ROOT_PASSWORDS.md
└── README.md
```

---

##  Contributing

Contributions of missing firmware images, changelogs, root exploits, or bootloader dumps are highly appreciated!

1. **Check Existing Files:** Make sure the firmware version isn't already archived in the respective folder.
2. **Follow Directory Hierarchy:** Place files in `<ISP>/<Vendor>/<Model>/`.
3. **Descriptive Filenames:** Retain the original OEM filename or include the exact firmware version string and Annex type (e.g., `Speedport_Plus_2_Sercomm_v2.9.003.4.bin`).
4. **Include Notes:** If a specific version has known bugs, changelogs, or unlocked root shells, please add a brief note on a `readme.md` on the model folder
5. **Open a Pull Request:** Submit your PR with relevant hardware revision info.

---

## Legal Disclaimer & Copyright

This repository is an independent community preservation archive and is **not** affiliated with, authorized, or endorsed by Vodafone Greece, COSMOTE / OTE, Nova, Wind, Deutsche Telekom, or any hardware OEM. 

All registered trademarks, product names, and company emblems belong to their respective holders and are used strictly under **Nominative Fair Use** for hardware identification and compatibility. All firmware files are provided on an **"AS IS"** basis for digital preservation, recovery, right-to-repair, and educational purposes.

**Read the full Legal Disclaimer & Notice:**
- 🇬🇧 **English:** [DISCLAIMER.md](DISCLAIMER.md)
- 🇬🇷 **Ελληνικά:** [DISCLAIMER_GR.md](DISCLAIMER_GR.md)
