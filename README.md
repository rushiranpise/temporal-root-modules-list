# Temporal Root Modules List

Community-maintained compatibility list for modules and tools tested with Temporal Root.

> Compatibility can vary depending on the device, ROM, Android version, Temporal Root version, module version, and other installed software.

## Status

| Status | Meaning |
|---|---|
| 🟢 Working | Confirmed working |
| 🟡 Partial | Partially working or has limitations |
| 🔴 Not Working | Confirmed not working |
| 🟠 Outdated | Marked outdated |
| ⚪ Needs Retest | Requires a new test |

## 🟢 Working

### AdBlocks / Firewalls / DNS Alternatives

| Module | Notes |
|---|---|
| [AdClose](https://github.com/zjyzip/AdClose) |  |
| [AdGuard Certificate](https://github.com/AdguardTeam/adguardcert) |  |
| [AFWall+](https://github.com/ukanth/afwall) |  |
| [bindhosts](https://github.com/bindhosts/bindhosts) |  |
| [Discover Ads Filter](https://github.com/hxreborn/discover-ads-filter) |  |

### Android Patches / Fixes / Bypass / BK

| Module | Notes |
|---|---|
| [CorePatch](https://github.com/LSPosed/CorePatch) | Confirmed buggy, soft bootloop |
| [IAmNotADeveloper](https://github.com/xfqwdsj/IAmNotADeveloper) |  |
| [Migrate-OSS](https://github.com/BaltiApps/Migrate-OSS) |  |
| [pairipfix](https://github.com/mezo123451A/pairipfix) |  |
| [Update Locker](https://github.com/Xposed-Modules-Repo/ru.mike.updatelocker/) |  |
| [Zygisk Detach](https://github.com/j-hc/zygisk-detach) |  |

### App Mods / Revanced / Morphe / Others

| Module | Notes |
|---|---|
| [amznkiller](https://github.com/hxreborn/amznkiller) |  |
| [Facebook App Ads Remover](https://github.com/Loukious/FacebookAppAdsRemover) |  |
| [NexAlloy](https://github.com/nexalloy/NexAlloy) |  |
| [Re:X (ReX)](https://github.com/Xposed-Modules-Repo/one.dot.rex) |  |
| [ReVancedXposed_Spotify](https://github.com/TheWinner02/ReVancedXposed_Spotify) |  |
| [WaDeepDark](https://github.com/Dhangofa/WaDeepDark) |  |
| [YouTube Revanced](https://github.com/Zy0x/YouTube-Revanced/) |  |

### Audio / DSPs / HAL

| Module | Notes |
|---|---|
| [ViPERFX_RE](https://github.com/likelikeslike/ViPERFX_RE) | PLEASE read the install process, flash with KernelSU |

### Base / Loaders / Frameworks

| Module | Notes |
|---|---|
| [LSPosed](https://github.com/KernelSU-Modules-Repo/zygisk_lsposed) | GPS apparently throws tantrum sometimes |
| [Vector](https://github.com/JingMatrix/Vector/releases) | Confirmed buggy, use LSPosed |
| [ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext) | Confirmed buggy, use LSPosed |

### Mounting / USB / File Managers

| Module | Notes |
|---|---|
| [DuckUSB](https://github.com/Bouteillepleine/DuckUSB) |  |
| [MT Manager](https://mt2.cn/download/) |  |

### OneUI System App Mods

| Module | Notes |
|---|---|
| [OneUI Settings Hook](https://github.com/HeheJuice/OneUI-Settings-Hook) |  |
| [OneUIX](https://github.com/SoClear/OneUIX) |  |

### Optimizers / Battery / Net / Performance

| Module | Notes |
|---|---|
| [AppManager](https://github.com/Muntashirakon/AppManager) |  |
| [Frosty](https://github.com/Drsexo/Frosty) | Buggy + Possible wake-lock issues |
| [net-switch](https://github.com/Rem01Gaming/net-switch) |  |
| [Scene](https://omarea.com/#/) |  |

## 🔴 Not Working

### Base / Root

| Module | Notes |
|---|---|
| [Magisk](https://github.com/topjohnwu/Magisk) | Major problem, permanent hardbrick |

### Kernel / GPU

| Module | Notes |
|---|---|
| [KonaBess-Next](https://github.com/KonaBess-Next/KonaBess-Next) | Major problem, permanent hardbrick |

### Xposed

| Module | Notes |
|---|---|
| [Enable Screenshot (formerly Disable FLAG_SECURE)](https://modules.lsposed.org/module/io.github.lsposed.disableflagsecure/) | Not working, reboots device |
| [PrivacySpace](https://github.com/Xposed-Modules-Repo/cn.geektang.privacyspace) | Not working |

### Zygisk

| Module | Notes |
|---|---|
| [NeoZygisk](https://github.com/JingMatrix/NeoZygisk) | Not working, reboots device |
| [ReZygisk](https://github.com/PerformanC/ReZygisk) | Not working, reboots device |
| [Treat-Wheel-Zygisk](https://github.com/PerformanC/Treat-Wheel-Zygisk) | Not working, reboots device |

## 🟠 Outdated

### Kernel / GPU

| Module | Notes |
|---|---|
| [KonaBess](https://github.com/libxzr/KonaBess) | Outdated |

## Find New Modules

Looking for modules to test with Temporal Root? These sources can help you discover new modules and projects:

- [GitDroid](https://t.me/gitdroid)
- [Xposed Modules](https://rushiranpise.github.io/xposed-modules/)
- [Shizuku Modules](https://rushiranpise.github.io/shizuku-modules/)
- [LSPosed Modules Repository](https://modules.lsposed.org/)
- [Magisk Modules Repo](https://github.com/magisk-modules-repo)
- [Magisk Modules Alt Repo](https://github.com/Magisk-Modules-Alt-Repo/)
- [Androidacy Magisk Modules Repository](https://www.androidacy.com/magisk-modules-repository/)
- [Yuki](https://github.com/carlelieser/yuki)
- [ShizuCoreFetch](https://github.com/elhizazi1/ShizuCoreFetch)

These are discovery sources only. A module should be tested with Temporal Root before being added to this list.

## Add a Module

Found a module that you tested with Temporal Root?

Create a new module file in `modules/` and submit a pull request.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the required format.

## Update a Module

If compatibility changes, submit a pull request with the new test result and environment details.

## Source

The initial module list was imported from the [XDA Developers Temporal Root testing thread](https://xdaforums.com/t/list-of-modules-working-on-temporal-root.4796105/).
