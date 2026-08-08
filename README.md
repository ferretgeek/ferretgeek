<p align="center">
  <img src="./assets/profile-hero.png" alt="Ferret — 让复杂系统变得清楚、可靠、可用 / Clear tools for complicated systems" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI--first-0f766e?style=flat-square" alt="AI-first" />
  <img src="https://img.shields.io/badge/Self--hosted-0369a1?style=flat-square" alt="Self-hosted" />
  <img src="https://img.shields.io/badge/Open_source-6d28d9?style=flat-square" alt="Open source" />
  <img src="https://img.shields.io/badge/Windows_%2B_Linux-334155?style=flat-square" alt="Windows and Linux" />
</p>

<p align="center">
  <strong>把复杂的部署、运维与用量数据，做成真正清楚、可靠、普通人也能使用的产品。</strong><br />
  <em>I turn complicated deployment, operations, and usage data into clear, dependable products people can actually use.</em>
</p>

---

## 开源产品 / Open-source products

### 01 · [CPA-X](https://github.com/ferretgeek/CPA-X)

[![GitHub stars](https://img.shields.io/github/stars/ferretgeek/CPA-X?style=flat-square&label=Stars)](https://github.com/ferretgeek/CPA-X/stargazers)
[![Latest release](https://img.shields.io/github/v/release/ferretgeek/CPA-X?style=flat-square&label=Release)](https://github.com/ferretgeek/CPA-X/releases/latest)

<a href="https://github.com/ferretgeek/CPA-X">
  <img src="./assets/projects/cpa-x.png" alt="CPA-X CLIProxyAPI 管理面板预览 / CPA-X CLIProxyAPI admin panel preview" width="100%" />
</a>

**给 CLIProxyAPI 一套看得清、管得住、更新不心慌的控制台。** 这是一个面向真实自托管环境的 AI-first 管理面板，把服务状态、请求与费用、日志、配置检查和版本维护放进同一个清晰界面。

**A control plane for CLIProxyAPI that is easy to read, safe to operate, and calm to update.** This AI-first panel brings service health, requests and cost, logs, configuration checks, and release maintenance into one clear interface for real self-hosted environments.

- **运行全景 / Operational clarity** — 同时查看服务健康、CPU、内存、磁盘、请求、Token、费用与日志。<br />See service health, CPU, memory, disk, requests, tokens, estimated cost, and logs in one place.
- **安全更新 / Safer updates** — SHA-256 校验、原子替换、真实管理接口健康检查、失败回滚与版本退避。<br />Update with SHA-256 verification, atomic replacement, authenticated health checks, rollback, and failed-version backoff.
- **灵活部署 / Flexible deployment** — 覆盖 Linux/systemd、Windows 与 Docker 监控模式，并为 AI Agent 提供可执行文档。<br />Run on Linux/systemd, Windows, or in Docker monitoring mode, with executable guidance designed for AI agents.

**技术 / Stack** — `Python` · `Flask` · `Waitress` · `Docker` · `GitHub Actions`

[项目 / Repository](https://github.com/ferretgeek/CPA-X) · [下载 / Releases](https://github.com/ferretgeek/CPA-X/releases/latest) · [中文文档 / Chinese docs](https://github.com/ferretgeek/CPA-X/blob/main/README_CN.md) · [讨论 / Discussions](https://github.com/ferretgeek/CPA-X/discussions)

---

### 02 · [Codex Orbit](https://github.com/ferretgeek/CodexOrbit)

[![GitHub stars](https://img.shields.io/github/stars/ferretgeek/CodexOrbit?style=flat-square&label=Stars)](https://github.com/ferretgeek/CodexOrbit/stargazers)
[![Latest release](https://img.shields.io/github/v/release/ferretgeek/CodexOrbit?style=flat-square&label=Release)](https://github.com/ferretgeek/CodexOrbit/releases/latest)

<a href="https://github.com/ferretgeek/CodexOrbit">
  <img src="./assets/projects/codex-orbit.png" alt="Codex Orbit 桌面额度悬浮窗预览 / Codex Orbit desktop quota widget preview" width="100%" />
</a>

**把 Codex 主额度变成桌面上一眼可读的轨道。** Codex Orbit 是一个轻量 Windows 悬浮窗，通过本机 `codex app-server` 显示 ChatGPT 套餐中的 Codex 主额度、重置时间和套餐倍率。

**Put your primary Codex quota into an orbit you can read at a glance.** Codex Orbit is a lightweight Windows widget that uses the local `codex app-server` to show the primary Codex quota, reset time, and plan multiplier from your ChatGPT subscription.

- **一眼可读 / Glanceable** — 迷你条、额度圆环或组合显示，支持多主题、透明度、置顶、鼠标穿透和全屏隐藏。<br />Choose a mini bar, quota ring, or both, with themes, opacity, always-on-top, click-through, and fullscreen hiding.
- **自动发现 / Runtime discovery** — 自动识别 Codex App、CLI、IDE 扩展、Windows 安装包和 WSL 运行时。<br />Automatically discovers Codex App, CLI, IDE extensions, Windows installations, and WSL runtimes.
- **隐私优先 / Privacy first** — 不读取 Codex 凭据、不要求复制 Token 或 API Key，也没有遥测。<br />Never reads Codex credentials, never asks you to copy a token or API key, and includes no telemetry.

**技术 / Stack** — `C#` · `WPF` · `.NET Framework 4.8` · `PowerShell`

[项目 / Repository](https://github.com/ferretgeek/CodexOrbit) · [下载 / Releases](https://github.com/ferretgeek/CodexOrbit/releases/latest) · [架构 / Architecture](https://github.com/ferretgeek/CodexOrbit/blob/main/docs/ARCHITECTURE.md) · [反馈 / Issues](https://github.com/ferretgeek/CodexOrbit/issues)

---

### 03 · [Codex Quota Overview](https://github.com/ferretgeek/codex-quota-overview)

[![GitHub stars](https://img.shields.io/github/stars/ferretgeek/codex-quota-overview?style=flat-square&label=Stars)](https://github.com/ferretgeek/codex-quota-overview/stargazers)
[![Latest release](https://img.shields.io/github/v/release/ferretgeek/codex-quota-overview?style=flat-square&label=Release)](https://github.com/ferretgeek/codex-quota-overview/releases/latest)

<a href="https://github.com/ferretgeek/codex-quota-overview">
  <img src="./assets/projects/codex-quota-overview.png" alt="Codex 额度总览批量扫描面板预览 / Codex Quota Overview bulk scanning dashboard preview" width="100%" />
</a>

**把散落的 Codex 账户额度，收进一个可查询的本地总览。** 这个 Windows 工具面向多账户和大规模本地认证文件场景，集中呈现总额度、剩余额度、重置窗口、账户状态与扫描结果。

**Bring scattered Codex account quotas into one searchable local overview.** This Windows tool is built for multiple accounts and large collections of local authentication files, presenting total quota, remaining quota, reset windows, account health, and scan results together.

- **批量导入 / Bulk import** — 支持多次选择文件夹、递归扫描 JSON，并按 CPU 线程数推荐并发。<br />Select folders across multiple passes, scan JSON recursively, and use CPU-aware concurrency recommendations.
- **面向规模 / Built for scale** — 服务端分页加载大结果，结果落盘，刷新页面不会自动重新扫描。<br />Handle large result sets with server-side pagination and persisted results without surprise rescans on refresh.
- **清晰汇总 / Clear summaries** — 展示额度、重置窗口和账户明细，支持 CSV 导出与统计清理。<br />Review quota, reset windows, and account details, then export CSV or clear stored statistics when needed.

**技术 / Stack** — `Go` · `React` · `TypeScript` · `Vite`

[项目 / Repository](https://github.com/ferretgeek/codex-quota-overview) · [下载 / Releases](https://github.com/ferretgeek/codex-quota-overview/releases/latest) · [使用说明 / Guide](https://github.com/ferretgeek/codex-quota-overview/blob/main/README.md) · [反馈 / Issues](https://github.com/ferretgeek/codex-quota-overview/issues)

---

### 04 · [LanPlay](https://github.com/ferretgeek/LanPlay)

[![GitHub stars](https://img.shields.io/github/stars/ferretgeek/LanPlay?style=flat-square&label=Stars)](https://github.com/ferretgeek/LanPlay/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/ferretgeek/LanPlay/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/ferretgeek/LanPlay/actions/workflows/ci.yml)

<a href="https://github.com/ferretgeek/LanPlay">
  <img src="./assets/projects/lanplay.png" alt="LanPlay 局域网 SMB 播放器预览 / LanPlay local-network SMB media player preview" width="100%" />
</a>

**把 SMB 共享变成 Android 里的本地私人影院。** LanPlay 直接浏览和播放局域网媒体，把字幕、音轨、续播、历史、标签和备份放进同一个原生应用，不要求账号或云端媒体库。

**Turn an SMB share into a private local cinema on Android.** LanPlay browses and plays media directly over the local network, combining subtitles, audio tracks, resume state, history, tags, and backups without requiring an account or cloud library.

- **原生 SMB 工作流 / Native SMB workflow** — 局域网发现、访客或账号连接、目录浏览、搜索和排序。<br />Discover shares, connect as a guest or user, then browse, search, and sort folders.
- **兼容播放 / Resilient playback** — Media3 主内核配合 libVLC 回退，支持硬解、倍速、画面适配及外挂字幕。<br />Use Media3 by default with libVLC fallback, hardware decoding, speed controls, scaling, and external subtitles.
- **隐私优先 / Privacy first** — 无账号、云同步或遥测；凭据仅在设备本地加密保存，公开预览全部匿名。<br />No account, cloud sync, or telemetry; credentials stay encrypted on-device and every public preview is anonymous.

**技术 / Stack** — `Kotlin` · `Jetpack Compose` · `Media3` · `libVLC` · `SMBJ` · `Python`

[项目 / Repository](https://github.com/ferretgeek/LanPlay) · [使用说明 / Guide](https://github.com/ferretgeek/LanPlay/blob/main/README.md) · [安全 / Security](https://github.com/ferretgeek/LanPlay/security) · [讨论 / Discussions](https://github.com/ferretgeek/LanPlay/discussions)

---

### 05 · [Vibe Prompt Recorder](https://github.com/ferretgeek/VibePromptRecorder)

[![GitHub stars](https://img.shields.io/github/stars/ferretgeek/VibePromptRecorder?style=flat-square&label=Stars)](https://github.com/ferretgeek/VibePromptRecorder/stargazers)
[![CI](https://img.shields.io/github/actions/workflow/status/ferretgeek/VibePromptRecorder/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/ferretgeek/VibePromptRecorder/actions/workflows/ci.yml)

<a href="https://github.com/ferretgeek/VibePromptRecorder">
  <img src="./assets/projects/vibe-prompt-recorder.png" alt="Vibe Prompt Recorder 本地提示词时间线预览 / Vibe Prompt Recorder local prompt timeline preview" width="100%" />
</a>

**把每一轮提示词，留在自己的本地时间线。** 这是一个离线 Windows 提示词工作台，用项目、草稿、轮次、搜索和 Markdown 编辑整理 Vibe Coding 过程，不接入模型 API，也不会上传内容。

**Keep every prompt iteration in your own local timeline.** This offline Windows workspace organizes Vibe Coding with projects, drafts, iterations, search, and Markdown editing—without calling a model API or uploading content.

- **轮次工作流 / Iteration workflow** — 草稿自动保存，一键完成当前轮并继续下一轮，完整上下文始终可回看。<br />Autosave drafts, complete the current iteration, and continue while keeping the full context available.
- **可靠本地数据 / Reliable local data** — SQLite WAL、原子写入、关闭保护、冲突处理、备份恢复和目录迁移。<br />Protect local work with SQLite WAL, atomic writes, close guards, conflict handling, backup, restore, and migration.
- **双模式编辑 / Two editing modes** — 所见即所得与 Markdown 源码模式，配合代码高亮、安全预览和全局搜索。<br />Switch between WYSIWYG and Markdown source with syntax highlighting, sanitized previews, and global search.

**技术 / Stack** — `Tauri 2` · `Rust` · `React` · `TypeScript` · `SQLite` · `Vite`

[项目 / Repository](https://github.com/ferretgeek/VibePromptRecorder) · [使用说明 / Guide](https://github.com/ferretgeek/VibePromptRecorder/blob/main/README.md) · [安全 / Security](https://github.com/ferretgeek/VibePromptRecorder/security) · [讨论 / Discussions](https://github.com/ferretgeek/VibePromptRecorder/discussions)

---

## 能力地图 / Capability map

<p align="center">
  <img src="./assets/capability-map.png" alt="Ferret 产品、全栈、桌面、运维与交付能力地图 / Ferret product, full-stack, desktop, operations, and delivery capability map" width="100%" />
</p>

五个项目覆盖了从产品梳理、界面设计、全栈、Android 与 Windows 桌面开发，到局域网媒体、可靠本地数据、部署、更新、验证、发布和 AI Agent 文档的完整链路。

Together, the five projects demonstrate an end-to-end product path—from product framing, interface design, full-stack, Android, and Windows desktop development to local-network media, reliable local data, deployment, safe updates, verification, releases, and agent-ready documentation.

---

## 我怎样做产品 / How I build

- **复杂留在系统里，清楚留给使用者。 / Keep complexity in the system and clarity at the surface.** 先把真实流程、失败模式和数据边界想清楚，再把它们压缩成容易理解的界面与操作。 / Understand the real workflow, failure modes, and data boundaries first; then compress them into an interface people can understand.
- **可靠性是一种产品体验。 / Reliability is a product experience.** 健康检查、校验、回滚、退避、可诊断日志和明确限制，不是后台细节，而是“敢不敢用”的基础。 / Health checks, verification, rollback, backoff, diagnosable logs, and explicit limits are not backend trivia—they are why a product feels safe to use.
- **文档也必须能执行。 / Documentation should be executable.** 项目优先提供清楚的安装路径、验证方式、失败处理和对 AI Agent 友好的接手上下文。 / Every project prioritizes clear installation paths, verification steps, failure handling, and handoff context that AI agents can act on.

<p align="center">
  <img src="https://img.shields.io/badge/Python-14354C?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Go-075985?style=flat-square&logo=go&logoColor=white" alt="Go" />
  <img src="https://img.shields.io/badge/TypeScript-1D4ED8?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/React-0F172A?style=flat-square&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Rust-7C2D12?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/Tauri-1F2937?style=flat-square&logo=tauri&logoColor=24C8DB" alt="Tauri" />
  <img src="https://img.shields.io/badge/.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt=".NET" />
  <img src="https://img.shields.io/badge/Docker-1E40AF?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub_Actions-1F2937?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
</p>

## 支持与说明 / Support & notes

如果你遇到问题、希望提出功能建议或参与协作，请前往对应项目的 Issues 或 Discussions；这样上下文、版本和处理进度都能留在正确的位置。

For bugs, feature ideas, or collaboration, please use the relevant project's Issues or Discussions so context, versions, and progress stay with the right codebase.

> Codex Orbit 与 Codex Quota Overview 是社区维护的非官方项目，与 OpenAI 没有隶属、授权或背书关系。它们不会绕过任何额度限制。<br />
> Codex Orbit and Codex Quota Overview are unofficial community projects with no affiliation, authorization, or endorsement from OpenAI. They do not bypass any usage limits.

<p align="center">
  <strong>Open source should make difficult work feel possible.</strong><br />
  <sub>开源不只是公开代码，也应该让困难的事情真正变得可完成。</sub>
</p>
