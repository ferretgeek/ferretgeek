# ferret <img src="./assets/profile/seal.svg" alt="问心" width="19" height="29">

我做能自己部署的 AI 服务，也写断网照常用的桌面工具。　[English](https://github.com/ferretgeek/ferretgeek/blob/main/README_EN.md)

## [ProkBot Plus](https://github.com/ferretgeek/prokbot-plus)

把 Grok Bot 的服务端放在自己的 Linux 机器上，接自己选的模型。这是基于 ProkBot 的非官方项目，仅限非商业使用。

<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/topology-dark.svg"><img src="./assets/profile/topology-light.svg" width="600" alt="客户端连到自托管 Host；Host 调用模型接口，把需要操作电脑的任务交给独立的 Linux 桌面。"></picture>

我给上游补了 **Windows 客户端适配和 Android 外壳**，并在 OpenAI Chat Completions 之外接入 **OpenAI Responses 和 Anthropic Messages**。在 Ampere A1 真机上，ARM64 Host 搭配独立的 amd64 桌面，已跑通两轮对话和 VNC 操作。

[架构笔记](https://github.com/ferretgeek/prokbot-plus/blob/main/docs/ARCHITECTURE.md) · [Android 实拍](https://github.com/ferretgeek/prokbot-plus/blob/main/docs/images/android-chat-zh.png) · [更新记录](https://github.com/ferretgeek/prokbot-plus/blob/main/CHANGELOG.md)

### 其他作品

- **[CPA-X](https://github.com/ferretgeek/cliproxyapi-dashboard)**：给 CLIProxyAPI 管升级。在 Linux / systemd 上，新版本重启后过不了健康检查，就自动回滚。
- **[LLM API Benchmark](https://github.com/ferretgeek/llm-api-benchmark)**：把首字延迟和输出速度分开测。预热请求算进成本，不算进速度成绩。
- **[提示词手账](https://github.com/ferretgeek/prompt-journal)**：用 Tauri 和 SQLite 按轮次保存提示词。离线可用，崩溃后能找回草稿。

[全部仓库](https://github.com/ferretgeek?tab=repositories) · [个人网站](https://ferretgeek.github.io/) · [来信](mailto:ferretgeek@vip.qq.com)
