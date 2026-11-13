# ferret <img src="./assets/profile/seal.svg" alt="Wenxin seal" width="19" height="29">

I build self-hosted AI services and offline desktop tools. · [中文](https://github.com/ferretgeek)

## [ProkBot Plus](https://github.com/ferretgeek/prokbot-plus)

Run the Grok Bot backend on your own Linux machine, with a model you choose. An unofficial extension of ProkBot for noncommercial use.

<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/profile/topology-dark.svg"><img src="./assets/profile/topology-light.svg" width="600" alt="Clients connect to a self-hosted Host. It calls the model API and delegates computer tasks to a separate Linux desktop."></picture>

I added **Windows client support and a custom Android shell**, then extended the upstream Chat Completions adapter to speak **OpenAI Responses and Anthropic Messages**. On Ampere A1 hardware, the ARM64 Host and a separate amd64 desktop completed a two-turn conversation and a VNC control test.

[Architecture notes](https://github.com/ferretgeek/prokbot-plus/blob/main/docs/ARCHITECTURE.en.md) · [Android screenshot](https://github.com/ferretgeek/prokbot-plus/blob/main/docs/images/android-chat-en.png) · [Changelog](https://github.com/ferretgeek/prokbot-plus/blob/main/CHANGELOG.md)

### Selected tools

- **[CPA-X](https://github.com/ferretgeek/cliproxyapi-dashboard)** upgrades CLIProxyAPI on Linux with systemd. If the new service fails its health check, it rolls back automatically.
- **[LLM API Benchmark](https://github.com/ferretgeek/llm-api-benchmark)** separates time to first token from output speed. Warm-up requests count toward cost, not speed.
- **[Prompt Journal](https://github.com/ferretgeek/prompt-journal)** keeps each revision of a prompt offline in a Tauri and SQLite desktop app. Drafts survive a crash.

[All repositories](https://github.com/ferretgeek?tab=repositories) · [Personal site](https://ferretgeek.github.io/?lang=en) · [Email](mailto:ferretgeek@vip.qq.com)
