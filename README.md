<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/toolbox-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/toolbox-light.svg">
  <img src="./assets/toolbox-light.svg" alt="ferret 的开源工具箱 — AI、邮箱、影音网络与帕鲁工具" width="100%">
</picture>

中文 · [English](./README_EN.md)

把自己遇到的小麻烦，做成能用的工具。这里收录了我的 **18 个开源项目**，按用途整理。

[AI 工具](#user-content-ai-工具) · [邮箱工具](#user-content-邮箱工具) · [影音与网络](#user-content-影音与网络) · [帕鲁工具](#user-content-帕鲁工具)

## AI 工具

| 项目 | 帮你做什么 |
| :--- | :--- |
| [Codex 额度悬浮窗](https://github.com/ferretgeek/codex-quota-widget) | 在 Windows 桌面查看 Codex 剩余额度和重置时间。 |
| [Codex 多账号额度总览](https://github.com/ferretgeek/codex-quota-overview) | 一次查看多个 Codex 账号的额度，导出表格。 |
| [提示词手账](https://github.com/ferretgeek/prompt-journal) | 保存和搜索每一轮提示词，方便回顾、复用和备份。 |
| [Obsidian AI 写作助手](https://github.com/ferretgeek/obsidian-ai-writer) | 让 AI 参考你选中的笔记写作，修改先预览再保存。 |
| [AI 接口测速工具](https://github.com/ferretgeek/llm-api-benchmark) | 比较 AI 接口的响应等待时间、输出速度和估算费用。 |
| [CLIProxyAPI 管理面板 · CPA-X](https://github.com/ferretgeek/cliproxyapi-dashboard) | 查看已部署服务的状态、账号和日志；Linux 下可管理升级。 |
| [CLIProxyAPI 账号检查工具](https://github.com/ferretgeek/cliproxyapi-credential-check) | 查看账号启用状态，可选检测可用性和额度。 |

## 邮箱工具

| 项目 | 帮你做什么 |
| :--- | :--- |
| [邮箱别名生成器](https://github.com/ferretgeek/email-alias-generator) | 为已有邮箱生成带标签的收件地址，方便区分注册来源。 |
| [Apple 隐藏邮件地址管理](https://github.com/ferretgeek/hide-my-email-manager) | 整理已创建的隐藏地址，添加标签、搜索和备份。 |
| [iCloud 验证码查找](https://github.com/ferretgeek/icloud-code-finder) | 从 iCloud 最近收到的邮件中查找并复制验证码。 |
| [Outlook 批量收件台](https://github.com/ferretgeek/outlook-batch-inbox) | 集中查看多个已授权 Outlook 邮箱的新邮件和验证码。 |
| [Outlook 授权续期工具](https://github.com/ferretgeek/outlook-token-keeper) | 定时刷新已有邮箱授权，检查连接状态和失败记录。 |
| [邮件取件链接](https://github.com/ferretgeek/imap-pickup-links) | 给已有邮箱生成可撤销的网页取件链接。 |
| [自建域名收件箱](https://github.com/ferretgeek/domain-mail-inbox) | 在自己的服务器上，为自己的域名搭建网页收件箱。 |

## 影音与网络

| 项目 | 帮你做什么 |
| :--- | :--- |
| [局域网视频播放器](https://github.com/ferretgeek/android-smb-player) | 用 Android 手机播放电脑或 NAS 共享文件夹里的视频。 |
| [代理节点可用性监测](https://github.com/ferretgeek/proxy-uptime-monitor) | 持续检查代理节点能否真正打开目标网页，查看故障记录。 |

## 帕鲁工具

| 项目 | 帮你做什么 |
| :--- | :--- |
| [帕鲁配种助手](https://github.com/ferretgeek/palworld-breeding-atlas) | 查询配种关系，从已有帕鲁规划目标路线，可读取存档。 |
| [帕鲁服务器管理面板](https://github.com/ferretgeek/palworld-server-panel) | 管理已搭好的 Linux 帕鲁服务器：状态、设置、备份与更新。 |

<details>
<summary><b>第一次用 GitHub？从这里开始</b></summary>

- **想先试一个简单工具：** 邮箱别名生成器可以下载完整源码并解压后，用浏览器打开 `index.html`。它生成地址，不创建新邮箱；收信前要确认邮箱支持标签地址。
- **想直接运行桌面工具：** 两个 Codex 额度工具都有 Windows 发布包。进入项目后找「下载」或 **Releases**，并先阅读账号和运行环境要求。
- **想用 Obsidian 插件：** 在 Obsidian AI 写作助手的项目页按步骤安装插件，再配置自己的模型服务。
- **其他工具怎么运行：** 部分项目需要 Python 等运行环境，少数需要源码编译或服务器部署。局域网视频播放器、提示词手账目前需要源码构建；各项目首页会说明具体条件。

项目页的 **README** 是使用说明，**Releases** 是已发布的版本，**Issues** 用来反馈问题。截图和详细步骤都放在各自的项目页里。

</details>

---

有问题或建议，欢迎到对应项目的 Issues 留言。
