<p align="center">
  <img src="./assets/profile-hero.png" alt="ferret — tools I built because something kept annoying me" width="100%" />
</p>

<p align="center">
  <a href="./README.md">中文</a> · <b>English</b>
</p>

## Hi

Every project here started the same way: something annoyed me enough times that I finally built a tool for it.

I wanted to watch a movie stored on my desktop, from my phone, without copying it first. I ran a Palworld server and never felt sure whether a settings change would break it. I had a pile of mailboxes to pull verification codes from, and doing it by hand took half an hour. None of that is hard. All of it is tedious. By the third time, I write a tool.

So the list looks scattered — a Palworld breeding planner next to an Outlook token renewer. But they share three things:

- **They run on your own machine.** No sign-up, no dependency on somebody's service staying alive.
- **Your data stays there.** Mail, saves, prompts, credentials — all local. No telemetry, no "anonymous analytics."
- **Uninstalling doesn't take your data with it.** Everything exports, everything backs up.

Some of them need no coding at all (marked 🟢 below). The rest ask you to open a terminal and paste one command.

---

## A few worth a closer look

### 1 · CPA-X — CLIProxyAPI admin dashboard

<a href="https://github.com/ferretgeek/cliproxyapi-dashboard">
  <img src="./assets/projects/cpa-x.png" alt="CPA-X admin dashboard" width="100%" />
</a>

[CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) turns Codex, Claude Code, and Gemini CLI subscriptions into standard API endpoints, and a lot of people use it to pool the accounts they already have. Getting it running is the easy part. Living with it is the problem: **which account is rate-limited right now? where did this month's tokens actually go? and after that upgrade, is the service still alive?**

CPA-X puts those answers on one page. It reads CLIProxyAPI's own logs and management API to show live request volume, per-model token and cost breakdowns, and per-account state — and it takes over the upgrade path.

> **Worth noting technically:** auto-update doesn't call itself successful just because a download finished. It verifies SHA-256, replaces files atomically, and then actually hits the authenticated management endpoint for an HTTP 200 before declaring success; failures get durable exponential backoff and a rollback. Logs are parsed incrementally rather than re-read, and offset-less timestamps are inferred correctly even when host and container time zones disagree. The config area is read-only by default — writing back to the main config requires explicitly setting `CLIPROXY_PANEL_CONFIG_WRITE_ENABLED`.

`Python` · `Flask` · Linux / Windows / Docker · ⭐ 62

[Repository](https://github.com/ferretgeek/cliproxyapi-dashboard) · [Releases](https://github.com/ferretgeek/cliproxyapi-dashboard/releases/latest) · [Docs](https://github.com/ferretgeek/cliproxyapi-dashboard/blob/main/README.md)

---

### 2 · SMB video player for Android 🟢

<a href="https://github.com/ferretgeek/android-smb-player">
  <img src="./assets/projects/lanplay.png" alt="Android SMB video player" width="100%" />
</a>

Your movies live on a desktop or a NAS. To watch them on a phone or tablet, you normally either copy a file over or stand up a whole media server.

You don't have to. A Windows shared folder, a Synology box, anything speaking SMB — this app connects and plays. Subtitles are matched automatically (and you can switch the character set when they come out garbled), playback position is remembered, and history, bookmarks, and tags all stay on the device. **No account, no cloud, no transcoding server.**

> **Worth noting technically:** SMB 2/3 is implemented natively — no WebDAV bridge, no third-party gateway. Playback runs on two engines: Media3 by default, with an automatic fallback to libVLC for awkward codecs, plus hardware decoding, speed control, and frame-rate matching. Credentials are encrypted on-device and logs are redacted. There's also an optional desktop scraper that writes posters and metadata back into the share ahead of time; the phone only reads the result, so nothing extra has to keep running.

`Kotlin` · `Jetpack Compose` · `Media3` · `libVLC` · Android 8+

[Repository](https://github.com/ferretgeek/android-smb-player) · [Guide](https://github.com/ferretgeek/android-smb-player/blob/main/README.md)

---

### 3 · Palworld breeding atlas 🟢

<a href="https://github.com/ferretgeek/palworld-breeding-atlas">
  <img src="./assets/projects/palworld-breeding-atlas.png" alt="Palworld breeding atlas" width="100%" />
</a>

Breeding charts for Palworld are everywhere, and all of them tell you "A + B = C." That isn't the question you actually have. The question is: **given what's in my base right now, what's the fastest path — and do I need to go catch something first?**

This reads your own save (read-only, never writes), sees what you actually own, and gives you steps you can follow: breed this, then this, and here's the one point where you'll have to go catch a missing parent. You can also ask it backwards — "from what I have, what's worth working toward?" No save required either: the 287-entry Paldeck and forty-thousand-plus breeding relationships are browsable on their own.

> **Worth noting technically:** `Level.sav` parsing is strictly read-only, with hard pre-parse ceilings on save input size, every zlib layer's output, and imported inventory JSON (all adjustable by environment variable) so a malformed save can't exhaust memory. Newer save formats need an Oodle DLL from a lawful local install — the repository doesn't ship it, and when it's missing you get a clear message instead of a silent failure. The same static bundle can be published as a self-hosted site via `server_publish.py`, reading the source save read-only and writing output through a temp directory with an atomic swap.

`Python` · Windows launcher + browser UI · fully offline

[Repository](https://github.com/ferretgeek/palworld-breeding-atlas) · [Data sources](https://github.com/ferretgeek/palworld-breeding-atlas/blob/main/docs/%E6%95%B0%E6%8D%AE%E6%9D%A5%E6%BA%90%E4%B8%8E%E6%9B%B4%E6%96%B0.md)

---

### 4 · Codex quota widget 🟢

<a href="https://github.com/ferretgeek/codex-quota-widget">
  <img src="./assets/projects/codex-orbit.png" alt="Codex quota desktop widget" width="100%" />
</a>

The worst moment when coding with Codex is running out of quota halfway through a thought.

This is a small always-on-top widget that shows how much Codex quota your ChatGPT plan has left and when it resets. It warns you when you're nearly out, and tells you when it's back. Show it as a compact bar, a ring, or make it click-through so it just sits in the background.

> **Worth noting technically:** it never reads `auth.json` and never asks you to paste a token. It spawns a hidden local `codex app-server` child process on demand and receives official quota notifications over stdio, leaving authentication and refresh entirely to Codex itself. When live notifications aren't available, it falls back to read-only tailing of `rate_limits` entries in recent session logs. Six runtimes are auto-discovered — Codex App, Codex CLI, `PATH`, IDE extensions, the Windows installer, and WSL — so having any one of them installed is enough.

`C#` · `WPF` · `.NET Framework 4.8` · Windows 10/11

[Repository](https://github.com/ferretgeek/codex-quota-widget) · [Releases](https://github.com/ferretgeek/codex-quota-widget/releases/latest) · [Architecture](https://github.com/ferretgeek/codex-quota-widget/blob/main/docs/ARCHITECTURE.en.md)

---

### 5 · Obsidian AI writing assistant 🟢

<a href="https://github.com/ferretgeek/obsidian-ai-writer">
  <img src="./assets/projects/vault-muse.png" alt="Obsidian AI writing assistant" width="100%" />
</a>

Most AI note plugins do two things that make them hard to trust: they quietly read your entire vault, and they edit your files directly.

This one works the other way around. You choose the context — these notes, this tag, this selection, this image — and every item stays listed beside the conversation where you can drop it. When it wants to change a note, you get a diff first and nothing is written until you confirm. Mistakes are undoable, and deletions only go to Obsidian's trash.

Bring your own endpoint: OpenAI Responses, any OpenAI-compatible Chat Completions API, Anthropic Messages, or a local Ollama.

> **Worth noting technically:** API keys and custom headers stay in memory by default, remote endpoints are forced to HTTPS, and dangerous headers are rejected outright. Write paths block traversal, absolute paths, `.trash`, and the vault config directory. Streaming replies, collapsible reasoning, image understanding, searchable and exportable history, slash workflows, and prompt caching are all implemented.

`TypeScript` · Obsidian 1.8.7+

[Repository](https://github.com/ferretgeek/obsidian-ai-writer) · [Live demo](https://ferretgeek.github.io/obsidian-ai-writer/) · [Privacy](https://github.com/ferretgeek/obsidian-ai-writer/blob/main/docs/PRIVACY.md)

---

## All 18 projects

🟢 = usable without writing any code

### AI and development

| Project | What it does | Stack |
|---|---|---|
| [**CPA-X** — CLIProxyAPI dashboard](https://github.com/ferretgeek/cliproxyapi-dashboard) ⭐62 | One page for account health, token spend, and whether that upgrade worked | `Python` `Flask` |
| [**Codex quota widget**](https://github.com/ferretgeek/codex-quota-widget) 🟢 | Desktop widget for live Codex quota and time until reset | `C#` `WPF` |
| [**Codex quota overview**](https://github.com/ferretgeek/codex-quota-overview) | Import dozens of auth files, check every account's quota, export CSV | `Go` `React` |
| [**CLIProxyAPI credential check**](https://github.com/ferretgeek/cliproxyapi-credential-check) | Which credentials in the pool are dead; read-only, with confirm-phrase actions | `Python` |
| [**LLM API benchmark**](https://github.com/ferretgeek/llm-api-benchmark) | Time to first token, sustained output speed, cache hits, and what it cost | `Python` `FastAPI` |
| [**Prompt journal**](https://github.com/ferretgeek/prompt-journal) 🟢 | Every prompt iteration you and the model worked through, offline and searchable | `Tauri` `Rust` `React` |
| [**Obsidian AI writer**](https://github.com/ferretgeek/obsidian-ai-writer) 🟢 | Chat over notes you chose; edits are shown as a diff before anything is written | `TypeScript` |

### Mail and privacy

| Project | What it does | Stack |
|---|---|---|
| [**Domain mail inbox**](https://github.com/ferretgeek/domain-mail-inbox) | Make your own domain actually receive mail at any `name@yourdomain` | `Python` stdlib · `SQLite` |
| [**IMAP pickup links**](https://github.com/ferretgeek/imap-pickup-links) | One revocable web link per mailbox, so someone else can collect a code | `Python` stdlib · `SQLite` |
| [**Outlook batch inbox**](https://github.com/ferretgeek/outlook-batch-inbox) | Read new mail and codes from up to 50 Microsoft mailboxes, OAuth only | `Python` stdlib |
| [**iCloud code finder**](https://github.com/ferretgeek/icloud-code-finder) | Pull verification codes out of recent iCloud mail and forget the password | `Python` stdlib |
| [**Hide My Email manager**](https://github.com/ferretgeek/hide-my-email-manager) 🟢 | Import, label, search, and back up the Apple aliases you already created | `Python` `SQLite` |
| [**Outlook token keeper**](https://github.com/ferretgeek/outlook-token-keeper) | Renew authorized OAuth tokens on schedule and verify mailboxes still connect | `Python` `FastAPI` `PostgreSQL` |
| [**Email alias generator**](https://github.com/ferretgeek/email-alias-generator) 🟢 | Bulk-generate `name+tag@domain` addresses entirely in the browser | `JavaScript` · no backend |

### Games

| Project | What it does | Stack |
|---|---|---|
| [**Palworld breeding atlas**](https://github.com/ferretgeek/palworld-breeding-atlas) 🟢 | The shortest breeding path from the Pals you already own | `Python` · offline |
| [**Palworld server panel**](https://github.com/ferretgeek/palworld-server-panel) | Status, world settings, backups, and updates for a server you host | `Python` `systemd` |

### Media and networking

| Project | What it does | Stack |
|---|---|---|
| [**Android SMB player**](https://github.com/ferretgeek/android-smb-player) 🟢 | Play video straight off a desktop or NAS share; subtitles and progress stay local | `Kotlin` `Media3` `libVLC` |
| [**Proxy uptime monitor**](https://github.com/ferretgeek/proxy-uptime-monitor) | Actually route through the proxy before calling a node healthy | `Python` `FastAPI` `sing-box` |

<details>
<summary><b>See the other 13 interfaces</b></summary>

<br />

Every screenshot below uses synthetic data generated specifically for public previews — no real account, message, save file, or host.

| | |
|---|---|
| [Prompt journal](https://github.com/ferretgeek/prompt-journal)<br /><img src="./assets/projects/vibe-prompt-recorder.png" width="100%" /> | [Palworld server panel](https://github.com/ferretgeek/palworld-server-panel)<br /><img src="./assets/projects/palworld-ops.png" width="100%" /> |
| [Codex quota overview](https://github.com/ferretgeek/codex-quota-overview)<br /><img src="./assets/projects/codex-quota-overview.png" width="100%" /> | [LLM API benchmark](https://github.com/ferretgeek/llm-api-benchmark)<br /><img src="./assets/projects/spectrum-bench.png" width="100%" /> |
| [CLIProxyAPI credential check](https://github.com/ferretgeek/cliproxyapi-credential-check)<br /><img src="./assets/projects/credential-compass.png" width="100%" /> | [Proxy uptime monitor](https://github.com/ferretgeek/proxy-uptime-monitor)<br /><img src="./assets/projects/trailmark.png" width="100%" /> |
| [Domain mail inbox](https://github.com/ferretgeek/domain-mail-inbox)<br /><img src="./assets/projects/ferret-mail.png" width="100%" /> | [IMAP pickup links](https://github.com/ferretgeek/imap-pickup-links)<br /><img src="./assets/projects/mail-ferry.png" width="100%" /> |
| [Outlook batch inbox](https://github.com/ferretgeek/outlook-batch-inbox)<br /><img src="./assets/projects/inboxharbor.png" width="100%" /> | [Outlook token keeper](https://github.com/ferretgeek/outlook-token-keeper)<br /><img src="./assets/projects/token-loom.png" width="100%" /> |
| [iCloud code finder](https://github.com/ferretgeek/icloud-code-finder)<br /><img src="./assets/projects/mail-lantern.png" width="100%" /> | [Hide My Email manager](https://github.com/ferretgeek/hide-my-email-manager)<br /><img src="./assets/projects/veil-garden.png" width="100%" /> |
| [Email alias generator](https://github.com/ferretgeek/email-alias-generator)<br /><img src="./assets/projects/alias-atelier.png" width="100%" /> | |

</details>

---

## How I build things

**Work out where people get stuck first.** Every empty state, loading state, error, and "wait, did I just break something?" moment needs an owner. Shipping the feature is only half of it.

**The default has to be the safe one.** Bind to localhost. Mask accounts and mail. Stay read-only when read-only is enough. For anything irreversible — disabling, deleting, exporting in full — require a typed confirmation phrase, not a dialog you can click through.

**A fake success is worse than a failure.** A backup has to restore (with a member manifest and hashes). An upgrade isn't done until a health check passes. A benchmark reports full `usage` and never dresses up concurrent throughput as single-request speed.

**Everything runs where you are.** Local and self-hosted modes share the same core logic and data format. There is no cloud-only edition.

**The interface deserves real work.** Every project with a UI ships a complete theme system — a deep-gray dark mode plus three to five light palettes — covering dialogs, tables, forms, editors, and every interaction state, and it remembers your choice. Phone layouts are fully usable, not merely reachable.

<details>
<summary><b>A hardening pass in August 2026 (for the technically curious)</b></summary>

<br />

Fifteen public projects went through a repository-by-repository threat model and source-to-sink review, focused on authentication and sessions, request-body and import resource budgets, trusted-proxy boundaries, SSRF and DNS rebinding, sensitive errors and log persistence, CSV formula injection, archive restore paths, concurrent lifecycle state, and CI supply chains.

All 51 confirmed issues were closed in code, tests, and maintenance docs. Privileged GitHub Actions are pinned to reviewed commits, and deployment defaults stay loopback-first, TLS-required for remote access, explicitly authenticated, and least-privilege.

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
  Ideas, questions, or want to build something together? Find me in that project's Issues or Discussions.
</p>

<p align="center">
  <sub>
  These are all independent community projects. The Codex and CLIProxyAPI tools are not affiliated with, authorized by, or endorsed by OpenAI, and they don't bypass any usage limit. The Palworld tools are not affiliated with Pocketpair. The Outlook, iCloud, and Hide My Email tools are not affiliated with Microsoft or Apple. All trademarks belong to their respective owners.
  </sub>
</p>
