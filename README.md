# Greek ISP Router Firmware Archive

[![Status](https://img.shields.io/badge/Status-Preservation%20Archive-blue.svg)](#)
[![Region](https://img.shields.io/badge/Region-Greece%20%F0%9F%87%AC%F0%9F%87%B7-1e88e5.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](#contributing)

<br/>

[![OTE](https://img.shields.io/badge/OTE-00458C?style=flat&logoColor=white)](Cosmote/)
[![Cosmote](https://img.shields.io/badge/Cosmote-008A00?style=flat&logoColor=white)](Cosmote/)
[![Telekom](https://img.shields.io/badge/Telekom-E20074?style=flat&logo=deutschetelekom&logoColor=white)](Cosmote/)
[![Vodafone](https://img.shields.io/badge/Vodafone-E60000?style=flat&logo=vodafone&logoColor=white)](Vodafone/)
[![Nova](https://img.shields.io/badge/Nova-000000?style=flat&logoColor=white)](Nova/)
[![Wind](https://img.shields.io/badge/Wind-009FE3?style=flat&logoColor=white)](Wind/)
[![Forthnet](https://img.shields.io/badge/Forthnet-F58220?style=flat&logoColor=white)](Forthnet/)
[![HOL](https://img.shields.io/badge/HOL-E30613?style=flat&logoColor=white)](HOL/)
[![Cyta](https://img.shields.io/badge/Cyta-792482?style=flat&logoColor=white)](Cyta/)

>A centralized, community-driven preservation repository archiving stock and ISP-customized firmware binaries, recovery images, and documentation for CPE routers, VoIP gateways, and modems distributed by Greek Internet Service Providers (both active and legacy).

---

## ToC

- [Why This Repository Exists](#why-this-repository-exists)
- [Root Passwords & Superuser Guide](#root-passwords--superuser-guide)
- [Provider & Hardware Catalog](#provider--hardware-catalog)
  - [1. Cosmote (OTE)](#1-cosmote-ote)
  - [2. Vodafone Greece](#2-vodafone-greece)
  - [3. Nova](#3-nova)
  - [4. Wind Hellas (Legacy)](#4-wind-hellas-legacy)
  - [5. Forthnet (Legacy)](#5-forthnet-legacy)
  - [6. HOL - Hellas On-Line (Legacy)](#6-hol---hellas-on-line-legacy)
  - [7. Cyta Hellas (Legacy)](#7-cyta-hellas-legacy)
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

### 1. Cosmote (OTE)
[![Cosmote](https://img.shields.io/badge/Cosmote-008A00?style=flat&logoColor=white)](Cosmote/)
[![OTE](https://img.shields.io/badge/OTE-00458C?style=flat&logoColor=white)](Cosmote/)
[![Telekom](https://img.shields.io/badge/Telekom-E20074?style=flat&logo=deutschetelekom&logoColor=white)](Cosmote/)  
*Folder: [`Cosmote/`](Cosmote/)*

| Manufacturer | Model / Device Name | Technology / Type | Notes |
| :--- | :--- | :--- | :--- |
| **Arcadyan** | [Speedport Plus 2](Cosmote/Arcadyan/Speedport_Plus_2/) | VDSL2 / Vectoring / VoIP | ⚠️ *Do not cross-flash with Sercomm Plus 2* |
| **Huawei** | [HA35-10](Cosmote/Huawei/HA35-10/) | VDSL2 + 4G Hybrid Access | Cosmote Home Booster (Bonded DSL + LTE) |
| **Intracom** | [JetSpeed 520](Cosmote/Intracom/Jetspeed_520/) | ADSL / ADSL2+ | Annex A & Annex B images |
| **Oxygen** | [HDI24201](Cosmote/Oxygen/HDI24201/), [HDI34201](Cosmote/Oxygen/HDI34201/) | VDSL2 / Multi-line VoIP / ISDN | Business PBX / Enterprise Gateways |
| **Sercomm** | [Speedport Plus 1](Cosmote/Sercomm/Speedport_Plus_1/) | VDSL2 35b / Vectoring / VoIP | Stock & rollback firmware |
| **Sercomm** | [Speedport Plus 2](Cosmote/Sercomm/Speedport_Plus_2/) | VDSL2 / Vectoring / VoIP | ⚠️ *Do not cross-flash with Arcadyan Plus 2* |
| **Sercomm** | [Speedport W 724V (Type Ci)](Cosmote/Sercomm/Speedport_W_724V_Type_Ci/) | VDSL2 / VoIP | Legacy Gigabit dual-band CPE |
| **ZTE** | [Speedport Entry 2i](Cosmote/ZTE/Speedport_Entry_2i/) | VDSL2 17a / VoIP | Popular workhorse VDSL router |
| **ZTE** | [ZXHN H108NS](Cosmote/ZTE/H108NS/) | ADSL2+ | Annex A & Annex B variants |
| **ZTE** | [ZXHN H1600](Cosmote/ZTE/H1600/) | VDSL2 35b / Wi-Fi 6 / VoIP | Includes [Firmware Changelog](Cosmote/ZTE/H1600/README.md) |

---

### 2. Vodafone Greece
[![Vodafone](https://img.shields.io/badge/Vodafone-E60000?style=flat&logo=vodafone&logoColor=white)](Vodafone/)  
*Folder: [`Vodafone/`](Vodafone/)*

Split into **Retail** (residential) and **OneNet** (business/enterprise) solutions:

#### Retail Solutions (`Vodafone/Retail/`)
| Manufacturer | Model / Device Name | Technology / Highlights |
| :--- | :--- | :--- |
| **Sercomm** | [H300s](Vodafone/Retail/Sercomm/H300s/) | VDSL2 35b / VoIP / AC1600 (Multiple firmware releases) |
| **Sercomm** | [Power Station Wi-Fi 6](Vodafone/Retail/Sercomm/Power_Station_WiFi6/) | VDSL2 35b / Wi-Fi 6 AX / VoIP (Vodafone Station 6) |
| **TP-Link** | [Archer VR100v](Vodafone/Retail/TP-LINK/100V/) | VDSL2 / VoIP Gateway |
| **Vantiva** | [Ultra Hub 7](Vodafone/Retail/Vantiva/Ultra_Hub_7/) | Wi-Fi 7 / FTTH & Ultra-broadband Gateway |
| **ZTE** | [ZXHN H108N (v2.5)](Vodafone/Retail/ZTE/H108N_v2.5/) | ADSL2+ |
| **ZTE** | [ZXHN H208N](Vodafone/Retail/ZTE/H208N/), [H267N](Vodafone/Retail/ZTE/H267N/) | VDSL2 / VoIP |
| **ZTE** | [ZXHN H267A](Vodafone/Retail/ZTE/H267A/) | VDSL2 17a / Dual-band AC / VoIP |
| **ZTE** | [ZXHN H268Q](Vodafone/Retail/ZTE/H268Q/), [H268Q Wi-Fi 6](Vodafone/Retail/ZTE/H268Q_WiFi6/) | VDSL2 35b / Wi-Fi 5 & Wi-Fi 6 / VoIP |
| **ZTE** | [ZXHN H367N](Vodafone/Retail/ZTE/H367N/) | VDSL2 / VoIP |
| **ZTE** | [MF289F](Vodafone/Retail/ZTE/MF289F/) | 4G+ / LTE Cat20 Gateway |

#### OneNet Business Solutions (`Vodafone/OneNet/`)
| Manufacturer | Models | Highlights |
| :--- | :--- | :--- |
| **Aethra** | BG8542(E)WAC, BG8544(E)WAC, SV6044EM, XV8800 series | Enterprise VoIP & Multi-WAN business routers |
| **Oxygen** | EIA03002, HPV05200/05400/15400, IVL32100, IVV14200/34200, OIA45402, OJV35800/55800, OLA55204 | Carrier-grade IP PBX & ISDN/VoIP gateways |
| **Sercomm** | H300s (OneNet variant) | Business-configured Sercomm router |
| **ZTE** | H267A, H268Q (WiFi 5 & WiFi 6 OneNet editions) | OneNet SIP trunking / voice firmware |

---

### 3. Nova
[![Nova](https://img.shields.io/badge/Nova-000000?style=flat&logoColor=white)](Nova/)  
*Folder: [`Nova/`](Nova/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **Huawei** | [DN8245V-70](Nova/Huawei/DN8245V-70/) | SuperVectoring 35b / Dual-Band Wi-Fi / VoIP Gateway |
| **ZTE** | [ZXHN H288A](Nova/ZTE/H288A/) | Gigabit VDSL2 35b / AC1600 / VoIP |
| **Zyxel** | [VMG1312-T20B](Nova/Zyxel/VMG1312-T20B/) | VDSL2 / Multi-WAN Router |
| **Zyxel** | [VMG8623-T50B](Nova/Zyxel/VMG8623-T50B/) | AC2400 Dual-Band VDSL2 / VoIP Gateway |

---

### 4. Wind Hellas (Legacy)
[![Wind](https://img.shields.io/badge/Wind-009FE3?style=flat&logoColor=white)](Wind/) *(Merged into Nova)*  
*Folder: [`Wind/`](Wind/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **Technicolor** | [DGA 4130](Wind/Technicolor/DGA4130/) | Broadcom-based VDSL2 35b gateway (Homeware / OpenWrt moddable) |
| **Technicolor** | [TG788v v3](Wind/Technicolor/TG788v_v3/) | VDSL2 Gateway |
| **Technicolor** | [TG789vac v2](Wind/Technicolor/TG789vac/) | Dual-band AC VDSL2 Gateway |
| **ZTE** | [ZXHN H108L](Wind/ZTE/H108L/) | ADSL2+ |
| **ZTE** | [ZXHN H288A](Wind/ZTE/H288A/) | VDSL2 35b / AC VoIP Gateway |
| **Zyxel** | [VMG8623-T50B](Wind/Zyxel/VMG8623-T50B/) | Dual-Band VDSL2 Gateway |

---

### 5. Forthnet (Legacy)
[![Forthnet](https://img.shields.io/badge/Forthnet-F58220?style=flat&logoColor=white)](Forthnet/) *(Rebranded to Nova)*  
*Folder: [`Forthnet/`](Forthnet/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **Huawei** | [DG8245V-10](Forthnet/Huawei/DG8245V-10/) | VDSL2 / AC VoIP Gateway |
| **Technicolor** | [TG788vn](Forthnet/Technicolor/TG788vn/), [TG788v v3](Forthnet/Technicolor/TG788v_V3/) | Classic Forthnet VDSL modems |
| **ZTE** | [ZXHN H108N v2.5](Forthnet/ZTE/H108N_v2.5/) | ADSL2+ router |
| **ZTE** | [ZXHN H288A](Forthnet/ZTE/H288A/) | VDSL2 35b / VoIP |

---

### 6. HOL - Hellas On-Line (Legacy)
[![HOL](https://img.shields.io/badge/HOL-E30613?style=flat&logoColor=white)](HOL/) *(Acquired by Vodafone)*  
*Folder: [`HOL/`](HOL/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **Alcatel-Lucent** | [CellPipe 7130](HOL/Alcatel/CellPipe_7130/) | Early VDSL2 / ADSL2+ gateway |
| **AVM (Fritz!)** | [Fritz!Box Fon WLAN 7140](HOL/Fritz/Box_7140/) | Annex A & Annex B German PBX router (HOL edition) |
| **Intracom** | [NetFasteR IAD](HOL/Intracom/Netfaster_IAD/) | Annex A & B VoIP gateway |
| **Intracom** | [NetFasteR IAD 2](HOL/Intracom/Netfaster_IAD2/), [IAD 3](HOL/Intracom/Netfaster_IAD3/) | Legendary Greek VoIP CPEs |
| **Technicolor** | [TD5136v2](HOL/Technicolor/TD5136v2/) | ADSL2+ router |
| **ZTE** | [ZXHN H108N v2.3](HOL/ZTE/H108N_v2.3/), [H168N](HOL/ZTE/H168N/) | ADSL2+ and VDSL2 gateways |

---

### 7. Cyta Hellas (Legacy)
[![Cyta](https://img.shields.io/badge/Cyta-792482?style=flat&logoColor=white)](Cyta/) *(Acquired by Vodafone)*  
*Folder: [`Cyta/`](Cyta/)*

| Manufacturer | Model | Description |
| :--- | :--- | :--- |
| **ZTE** | [ZXHN H208N](Cyta/ZTE/H208N/) | Cyta VDSL2 / VoIP Gateway |
| **ZTE** | [ZXHN H267N](Cyta/ZTE/H267N/) | Cyta VDSL2 / VoIP Gateway |

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
│   ├── Intracom/
│   ├── Oxygen/
│   ├── Sercomm/
│   └── ZTE/
├── Vodafone/
│   ├── Retail/
│   │   ├── Sercomm/
│   │   ├── TP-LINK/
│   │   ├── Vantiva/
│   │   └── ZTE/
│   └── OneNet/
│       ├── Aethra/
│       ├── Oxygen/
│       ├── Sercomm/
│       └── ZTE/
├── Nova/
│   ├── Huawei/
│   ├── ZTE/
│   └── Zyxel/
├── Wind/
│   ├── Technicolor/
│   ├── ZTE/
│   └── Zyxel/
├── Forthnet/
│   ├── Huawei/
│   ├── Technicolor/
│   └── ZTE/
├── HOL/
│   ├── Alcatel/
│   ├── Fritz/
│   ├── Intracom/
│   ├── Technicolor/
│   └── ZTE/
├── Cyta/
│   └── ZTE/
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
