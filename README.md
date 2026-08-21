<p align="center">
  <img src="./assets/profile-hero.png" alt="ferret — 自己遇到的麻烦，自己做个工具解决" width="100%" />
</p>

<p align="center">
  <b>中文</b> · <a href="./README_EN.md">English</a>
</p>

## 你好

这里的每一个项目，都是我自己先被某件事烦到了，才动手做的。

比如我在手机上想看电脑里的电影，得先传过去；比如我开了个帕鲁服务器，每次改设置都心里没底；比如我有一堆邮箱要收验证码，一个个登录要花半小时。这些事都不难，但都够烦。烦到第三次，我就会把它做成一个工具。

所以这些项目看起来八竿子打不着——一个是帕鲁配种表，一个是 Outlook 令牌续期。但它们有三件事是一样的：

- **装在自己的机器上就能用。** 不需要注册账号，不需要谁的服务器还活着。
- **你的东西不会离开这台机器。** 邮件、存档、提示词、账号，都留在本地。没有遥测，没有"匿名统计"。
- **删掉它，不会带走你的数据。** 所有东西都能导出，也都能备份。

不懂代码也能用其中一部分（下面标了 🟢）；剩下的需要你会开个终端、复制一条命令。

---

## 挑几个先看

### 1 · CPA-X — CLIProxyAPI 管理面板

<a href="https://github.com/ferretgeek/cliproxyapi-dashboard">
  <img src="./assets/projects/cpa-x.png" alt="CPA-X 管理面板界面" width="100%" />
</a>

[CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) 能把 Codex、Claude Code、Gemini CLI 的订阅额度变成标准 API，很多人拿它统一调度自己手上的几个号。麻烦不在跑起来，而在跑起来之后：**哪个号被限流了？这个月的 token 花在谁身上？我升级到新版本之后，服务到底还活着吗？**

CPA-X 把这几件事收进一个页面。它读 CLIProxyAPI 自己的日志和管理接口，展示实时请求量、按模型的 token 与成本、每个账号的状态，并接管升级流程。

> **技术上值得一提的：** 自动升级不是"下载完就报成功"——先校验 SHA-256、原子替换文件、真的去打一次带认证的管理接口拿到 HTTP 200 才算成功，失败则指数退避并回滚。日志按增量解析（不重读整个文件），支持宿主机与容器时区不一致时反推无偏移量的时间戳。配置区默认只读，主配置回写需要显式开 `CLIPROXY_PANEL_CONFIG_WRITE_ENABLED`。

`Python` · `Flask` · Linux / Windows / Docker · ⭐ 62

[仓库](https://github.com/ferretgeek/cliproxyapi-dashboard) · [下载](https://github.com/ferretgeek/cliproxyapi-dashboard/releases/latest) · [中文文档](https://github.com/ferretgeek/cliproxyapi-dashboard/blob/main/README_CN.md)

---

### 2 · 局域网影片播放器 🟢

<a href="https://github.com/ferretgeek/android-smb-player">
  <img src="./assets/projects/lanplay.png" alt="局域网影片播放器界面" width="100%" />
</a>

家里的电影都在电脑或 NAS 上，想在手机、平板上看，通常要么先传一份，要么装一整套媒体服务器。

其实不用。Windows 共享文件夹、群晖、任何开了 SMB 的设备，这个 App 直接连进去，点开就播。字幕会自动配对（乱码时可以换字符集），看到哪儿自动记住，历史、书签、标签都在手机本地。**没有账号，没有云，没有转码服务器。**

> **技术上值得一提的：** SMB 2/3 原生实现，不走 WebDAV 或第三方网关。播放走双内核——Media3 为主，遇到冷门编码自动回退 libVLC，支持硬解、倍速和帧率匹配。凭据在设备上加密保存，日志主动脱敏。另外附一个可选的 PC 端刮削器，提前生成海报和元数据写回共享目录，手机端只读结果，不额外开服务。

`Kotlin` · `Jetpack Compose` · `Media3` · `libVLC` · Android 8+

[仓库](https://github.com/ferretgeek/android-smb-player) · [使用说明](https://github.com/ferretgeek/android-smb-player/blob/main/README.md)

---

### 3 · 帕鲁配种图鉴 🟢

<a href="https://github.com/ferretgeek/palworld-breeding-atlas">
  <img src="./assets/projects/palworld-breeding-atlas.png" alt="帕鲁配种图鉴界面" width="100%" />
</a>

《幻兽帕鲁》里想要某只帕鲁，配种表在网上到处都有，但它们只告诉你"A + B = C"。真正的问题是：**我现在手上就这些，怎么配最快？中间要不要先去抓一只？**

这个工具读你自己的存档（只读，不改），看一眼你实际有什么，然后给出可执行的路线：先配什么、第几步会出什么、哪一步必须去补一只。也可以反过来问——"我手上这些，能配出什么值得练的"。不想连存档也行，287 只图鉴和四万多条配种关系可以直接翻。

> **技术上值得一提的：** `Level.sav` 的解析是纯只读的，zlib 每一层输出、存档输入体积和库存 JSON 都有解析前的硬上限（可通过环境变量放宽），避免畸形存档打爆内存。新格式存档需要系统里已合法安装的 Oodle DLL，仓库不分发它，找不到时会明确告知而不是静默失败。同一套静态资源可以用 `server_publish.py` 发布成自托管站点，源存档只读、输出走临时目录原子替换。

`Python` · Windows 启动器 + 浏览器界面 · 完全离线

[仓库](https://github.com/ferretgeek/palworld-breeding-atlas) · [数据来源](https://github.com/ferretgeek/palworld-breeding-atlas/blob/main/docs/%E6%95%B0%E6%8D%AE%E6%9D%A5%E6%BA%90%E4%B8%8E%E6%9B%B4%E6%96%B0.md)

---

### 4 · Codex 额度悬浮窗 🟢

<a href="https://github.com/ferretgeek/codex-quota-widget">
  <img src="./assets/projects/codex-orbit.png" alt="Codex 额度悬浮窗界面" width="100%" />
</a>

用 Codex 写代码的时候，最怕的是写到一半额度没了。

这是桌面上一个小小的悬浮窗，一直显示 ChatGPT 套餐里 Codex 还剩多少、几点回满。快用完了会提示你，回满了也会提示你。可以做成迷你条、圆环，或者干脆让鼠标穿过去当背景。

> **技术上值得一提的：** 它不读 `auth.json`，不要你复制任何 Token——而是按需拉起一个隐藏的本机 `codex app-server` 子进程，通过标准输入输出拿官方额度通知，认证和刷新全部交给 Codex 自己。服务端通知不可用时，退回只读扫描最近会话日志尾部的 `rate_limits` 记录兜底。Codex App、CLI、PATH、IDE 扩展、Windows 安装包和 WSL 六种运行时都会自动发现，装了任意一种就能用。

`C#` · `WPF` · `.NET Framework 4.8` · Windows 10/11

[仓库](https://github.com/ferretgeek/codex-quota-widget) · [下载](https://github.com/ferretgeek/codex-quota-widget/releases/latest) · [架构说明](https://github.com/ferretgeek/codex-quota-widget/blob/main/docs/ARCHITECTURE.md)

---

### 5 · Obsidian AI 写作助手 🟢

<a href="https://github.com/ferretgeek/obsidian-ai-writer">
  <img src="./assets/projects/vault-muse.png" alt="Obsidian AI 写作助手界面" width="100%" />
</a>

大部分 AI 笔记插件有两个让人不敢用的地方：它偷偷读了你整个库，以及它直接改了你的文件。

这个插件反过来做。上下文是你自己挑的——这几篇笔记、这个标签、这段选中的文字、这张图，每一项都列在旁边，随时能删掉。它要改笔记时先给你一份 diff，你点确认才写回；写错了能撤销，删除只进 Obsidian 废纸篓。

模型接口随你选：OpenAI Responses、任何 OpenAI 兼容接口、Anthropic Messages，或者本地跑的 Ollama。

> **技术上值得一提的：** API Key 与自定义 Header 默认只在内存中，远程接口强制 HTTPS，危险 Header 直接拒绝。写入路径挡掉路径穿越、绝对路径、`.trash` 和 Vault 配置目录。流式回复、思考过程折叠、图片理解、历史搜索与导出、斜杠工作流、提示词缓存都做完了。

`TypeScript` · Obsidian 1.8.7+

[仓库](https://github.com/ferretgeek/obsidian-ai-writer) · [在线演示](https://ferretgeek.github.io/obsidian-ai-writer/) · [隐私说明](https://github.com/ferretgeek/obsidian-ai-writer/blob/main/docs/PRIVACY.md)

---

## 全部 18 个项目

🟢 = 不用写代码也能上手

### AI 与开发

| 项目 | 一句话 | 技术栈 |
|---|---|---|
| [**CPA-X** · CLIProxyAPI 管理面板](https://github.com/ferretgeek/cliproxyapi-dashboard) ⭐62 | 一页看清哪个账号还活着、token 花在哪、升级有没有成功 | `Python` `Flask` |
| [**Codex 额度悬浮窗**](https://github.com/ferretgeek/codex-quota-widget) 🟢 | 桌面小窗随时显示 Codex 还剩多少、几点回满 | `C#` `WPF` |
| [**Codex 额度总览**](https://github.com/ferretgeek/codex-quota-overview) | 几十上百个号一次导入，批量查额度，导出 CSV | `Go` `React` |
| [**CLIProxyAPI 凭证体检**](https://github.com/ferretgeek/cliproxyapi-credential-check) | 凭证池里哪个号该换了，默认只读，停用要输确认短语 | `Python` |
| [**大模型接口测速台**](https://github.com/ferretgeek/llm-api-benchmark) | 首字等多久、每秒多少字、缓存命中多少、这次花了多少钱 | `Python` `FastAPI` |
| [**提示词手账**](https://github.com/ferretgeek/prompt-journal) 🟢 | 和 AI 一轮轮改出来的提示词，离线存本机，能搜能备份 | `Tauri` `Rust` `React` |
| [**Obsidian AI 写作助手**](https://github.com/ferretgeek/obsidian-ai-writer) 🟢 | 只读你指定的笔记，改动先给你看，确认才写回 | `TypeScript` |

### 邮箱与隐私

| 项目 | 一句话 | 技术栈 |
|---|---|---|
| [**自建域名收件箱**](https://github.com/ferretgeek/domain-mail-inbox) | 让自己的域名真能收信，任意 `名字@你的域名` 都收得到 | `Python` 标准库 `SQLite` |
| [**邮件取件链接**](https://github.com/ferretgeek/imap-pickup-links) | 每个邮箱一条独立网页链接，对方打开就能收码，随时撤销 | `Python` 标准库 `SQLite` |
| [**Outlook 批量收件台**](https://github.com/ferretgeek/outlook-batch-inbox) | 一次看 50 个 Outlook 邮箱的新邮件和验证码，只用 OAuth | `Python` 标准库 |
| [**iCloud 验证码查找**](https://github.com/ferretgeek/icloud-code-finder) | 从 iCloud 最近的邮件里直接捞出验证码，用完即忘 | `Python` 标准库 |
| [**隐私邮箱地址管理**](https://github.com/ferretgeek/hide-my-email-manager) 🟢 | Apple「隐藏邮件地址」建多了记不住，导入打标签搜索备份 | `Python` `SQLite` |
| [**Outlook 令牌续期**](https://github.com/ferretgeek/outlook-token-keeper) | 一批授权账号的令牌到期前自动续，并验证邮箱还连得上 | `Python` `FastAPI` `PostgreSQL` |
| [**邮箱别名生成器**](https://github.com/ferretgeek/email-alias-generator) 🟢 | 批量生成 `名字+标签@域名`，纯浏览器本地，什么都不上传 | `JavaScript` 纯前端 |

### 游戏

| 项目 | 一句话 | 技术栈 |
|---|---|---|
| [**帕鲁配种图鉴**](https://github.com/ferretgeek/palworld-breeding-atlas) 🟢 | 从手上现有的帕鲁出发，算出配到目标最省事的路线 | `Python` 离线 |
| [**帕鲁服务器面板**](https://github.com/ferretgeek/palworld-server-panel) | 自己开的服，网页里看状态、改设置、备份、更新 | `Python` `systemd` |

### 影音与网络

| 项目 | 一句话 | 技术栈 |
|---|---|---|
| [**局域网影片播放器**](https://github.com/ferretgeek/android-smb-player) 🟢 | 手机直接播电脑/NAS 共享里的影片，字幕进度都在本地 | `Kotlin` `Media3` `libVLC` |
| [**代理节点体检**](https://github.com/ferretgeek/proxy-uptime-monitor) | 真的走一遍代理再判断通不通，而不是 ping 一下就说好 | `Python` `FastAPI` `sing-box` |

<details>
<summary><b>展开看剩下 13 个的界面</b></summary>

<br />

以下截图全部来自专为开源展示生成的合成数据，不包含任何真实账号、邮件、存档或主机信息。

| | |
|---|---|
| [提示词手账](https://github.com/ferretgeek/prompt-journal)<br /><img src="./assets/projects/vibe-prompt-recorder.png" width="100%" /> | [帕鲁服务器面板](https://github.com/ferretgeek/palworld-server-panel)<br /><img src="./assets/projects/palworld-ops.png" width="100%" /> |
| [Codex 额度总览](https://github.com/ferretgeek/codex-quota-overview)<br /><img src="./assets/projects/codex-quota-overview.png" width="100%" /> | [大模型接口测速台](https://github.com/ferretgeek/llm-api-benchmark)<br /><img src="./assets/projects/spectrum-bench.png" width="100%" /> |
| [CLIProxyAPI 凭证体检](https://github.com/ferretgeek/cliproxyapi-credential-check)<br /><img src="./assets/projects/credential-compass.png" width="100%" /> | [代理节点体检](https://github.com/ferretgeek/proxy-uptime-monitor)<br /><img src="./assets/projects/trailmark.png" width="100%" /> |
| [自建域名收件箱](https://github.com/ferretgeek/domain-mail-inbox)<br /><img src="./assets/projects/ferret-mail.png" width="100%" /> | [邮件取件链接](https://github.com/ferretgeek/imap-pickup-links)<br /><img src="./assets/projects/mail-ferry.png" width="100%" /> |
| [Outlook 批量收件台](https://github.com/ferretgeek/outlook-batch-inbox)<br /><img src="./assets/projects/inboxharbor.png" width="100%" /> | [Outlook 令牌续期](https://github.com/ferretgeek/outlook-token-keeper)<br /><img src="./assets/projects/token-loom.png" width="100%" /> |
| [iCloud 验证码查找](https://github.com/ferretgeek/icloud-code-finder)<br /><img src="./assets/projects/mail-lantern.png" width="100%" /> | [隐私邮箱地址管理](https://github.com/ferretgeek/hide-my-email-manager)<br /><img src="./assets/projects/veil-garden.png" width="100%" /> |
| [邮箱别名生成器](https://github.com/ferretgeek/email-alias-generator)<br /><img src="./assets/projects/alias-atelier.png" width="100%" /> | |

</details>

---

## 我做东西的几条规矩

**先想清楚人会在哪一步卡住。** 界面上每一个空状态、加载中、出错、"我是不是点错了"，都要有人管。做完功能只是一半。

**默认值必须是安全的那一个。** 只监听本机；账号和邮件默认打码；能只读就只读；停用、删除、完整导出这类不可逆操作要求逐次输入确认短语——而不是"你确定吗"点一下就过。

**假的成功比失败更糟。** 备份要能真的恢复回来（带成员清单和哈希）；升级要真的打一次健康检查才算成功；测速要以完整 usage 为准，不能把并发吞吐伪装成单请求速度。

**每个项目都能装在你自己的地方。** 本地跑和自己服务器托管共享同一套核心逻辑与数据格式，不做只能用云的版本。

**界面值得认真做。** 每个带界面的项目都有一套完整主题（深灰暗色 + 三到五套浅色配色），覆盖弹窗、表格、表单、编辑器和全部交互状态，选择会记住。手机上也是完整可用，不是"能打开"。

<details>
<summary><b>2026 年 8 月的一次集中加固（技术读者向）</b></summary>

<br />

15 个公开项目做了一轮逐库威胁建模和从源到危险操作的数据流复核，重点在认证与会话、请求体与导入资源预算、可信代理边界、SSRF 与 DNS 重绑定、敏感错误与日志落盘、CSV 公式注入、归档恢复路径、并发生命周期状态，以及 CI 供应链。

确认的 51 个问题全部在代码、测试和维护文档里关闭。高权限 GitHub Actions 固定到审核过的 commit；部署默认值保持本机回环优先、远程强制 TLS、显式认证、最小权限。

</details>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-14354C?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Go-075985?style=flat-square&logo=go&logoColor=white" alt="Go" />
  <img src="https://img.shields.io/badge/TypeScript-1D4ED8?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Rust-7C2D12?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="C#" />
  <img src="https://img.shields.io/badge/Tauri-1F2937?style=flat-square&logo=tauri&logoColor=24C8DB" alt="Tauri" />
  <img src="https://img.shields.io/badge/Docker-1E40AF?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
</p>

<p align="center">
  有想法、有问题、想一起做，去对应项目的 Issues 或 Discussions 找我。
</p>

<p align="center">
  <sub>
  以上都是独立的社区项目。Codex 和 CLIProxyAPI 相关工具与 OpenAI 没有隶属、授权或背书关系，也不绕过任何额度限制；帕鲁相关工具与 Pocketpair 无关；Outlook、iCloud、Hide My Email 相关工具与 Microsoft、Apple 无关。各自的商标归其权利人所有。
  </sub>
</p>
