# Commerce & Family Sharing

Status: **aligned** — single one-time purchase; Family Sharing; price slightly under Wipr base.

## Model

| Item | Decision |
|------|----------|
| Store shape | **Free to download** + **one non-consumable IAP** unlocks everything |
| Unlock includes | Safari blocking, system-wide URL Filter, rule packs, ongoing list updates (one SKU; not a feature subscription) |
| Tips / donations | Not required for v1 |
| Family Sharing | **Yes** (enable on the unlock IAP; test non-purchaser family members) |
| Locked state | Onboarding, status, help visible; full blocking requires unlock — do **not** ship a second paid SKU for system-wide only |
| Not in v1 | Paid App Store download as primary; “Free Safari / paid system-wide” split; subscription for list updates |

## What is Family Sharing?（家庭共享）

Apple 的 **Family Sharing（家庭共享）** 让一个家庭组织里的成员（最多约 6 人）共享符合条件的 App 购买与部分内购。

对你们产品的意义：

- 组织里的**组织者（或有购买权限的人）买一次**，家庭中其他成员可在自己的设备上下载/使用同一 App 的共享购买，**不必每人再付一遍**（前提：该 App / IAP 在 App Store Connect 中开启了 Family Sharing）。
- 用户在系统设置里管理「家庭」；你们主要负责：在 Connect 里打开共享、产品文案写明支持、测试「非购买者成员能解锁」。
- 海外工具类（Wipr 等）常把它当信任与家庭向标配；和「买断制」很搭。

注意：

- 共享的是**购买权益**，不是把一个人的 iCloud 数据混在一起；你们仍是本地隐私、不采集浏览。
- 若用 **非消耗型 IAP** 解锁（而不是付费下载），需在该 IAP 上启用 Family Sharing，并做好恢复购买。
- 个别 IAP 类型或历史配置可能导致家庭成员需额外确认「购买共享」——上架前按当时的 App Store Connect 文档测一遍。

## Pricing policy

| Rule | Detail |
|------|--------|
| Anchor | **Wipr 2 base one-time price** on the App Store at ship time |
| Our price | **Slightly lower** than that anchor (target: about **$1 or less** below; not a deep discount) |
| What’s included | System-wide filtering is **in** the one-time price (not a Filtr-style core IAP) |
| Headline | Privacy, completeness, system-wide included — **not** “cheaper than Wipr” |
| Value story (secondary) | Same/near entry price as Wipr, but Filtr-class capability included → better total value vs Wipr + Filtr |

Concrete SKU number: fill in during App Store setup after checking live Wipr price.

## Competitive note

No absolute moat yet (incumbent has lists, reviews, rank). Pricing is **parity-minus-a-notch**, not a race to the bottom. Ranking is an outcome of quality and retention, not of undercutting alone.
