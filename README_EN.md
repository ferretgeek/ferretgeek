<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile-dark.svg">
  <img src="./assets/profile-light.svg" alt="ferret — Building complete software experiences from real needs" width="100%">
</picture>

[中文](./README.md) · English

# Hi, I'm ferret

**I build AI applications, automation services, and desktop / mobile software.**

I turn real-world requirements into software with clear interactions, deliberate data handling, and maintainable implementations. My open-source work spans requirements, interface design, APIs and storage, testing, packaging, deployment, and maintenance.

Beyond adding features, I focus on the engineering questions behind them: **How should AI performance be measured? How can interrupted jobs resume? What happens when an upgrade fails? Where should sensitive data live?** These projects show how I approach those questions.

[Selected projects](#user-content-selected-projects) · [Engineering practices](#user-content-engineering-practices) · [More projects](#user-content-more-projects)

## Selected projects

### [CPA-X · AI Service Management](https://github.com/ferretgeek/cliproxyapi-dashboard)

A management interface for an existing CLIProxyAPI deployment: inspect service status and request logs, and manage upgrades on Linux.

- **Implementation:** Incremental log parsing; upgrades use SHA-256 verification, atomic replacement, and real API health checks, with rollback on failure and retry backoff for failed versions.
- **Design rationale:** A running process is not necessarily a working service. Verify the actual endpoint before reporting success, and provide a recovery path when it fails.

`Python` · `Flask` · `Linux / systemd`

### [LLM API Performance Evaluation](https://github.com/ferretgeek/llm-api-benchmark)

Compare response latency, output speed, and estimated API cost under fixed test scenarios.

- **Implementation:** Parse streaming responses and track time to first text, output speed, and token usage separately. Keep warm-ups outside formal samples and interrupted estimates separate from complete usage.
- **Design rationale:** Concurrent throughput is not single-request speed, and an estimate is not a bill. Explicit measurement rules make results easier to interpret and reproduce.

`Python` · `Streaming APIs` · `Performance measurement`

### [Outlook Authorization Maintenance](https://github.com/ferretgeek/outlook-token-keeper)

Maintain explicitly authorized mailbox accounts, schedule authorization refreshes, check connectivity, and record exceptions that need attention.

- **Implementation:** Separate the Web application from a background Worker. Persist jobs and progress in PostgreSQL so a single Worker can resume after restart. Encrypt credentials with AES-256-GCM bound to each account and field.
- **Design rationale:** Batch work should not depend on an open browser. Encryption should also verify which account a secret belongs to, rejecting ciphertext moved to the wrong account or field.

`Python / FastAPI` · `PostgreSQL` · `OAuth 2.0` · `Docker`

### [Prompt Journal · Local-First Desktop Application](https://github.com/ferretgeek/prompt-journal)

Organize AI collaboration prompts by project and iteration, with editing, search, export, and backups stored on the user's computer.

- **Implementation:** A React interface backed by Rust application logic; SQLite WAL and transactions, revision-based conflict detection, atomic file writes, close protection, and recovery workflows.
- **Design rationale:** Autosave is only part of persistence. Concurrent edits, unexpected exits, and data migration also need explicit handling to reduce silent overwrites and data loss.

`TypeScript / React` · `Rust / Tauri 2` · `SQLite`

### [Android LAN Video Player](https://github.com/ferretgeek/android-smb-player)

Play videos directly from a computer or NAS share without copying files first or deploying an additional transcoding service.

- **Implementation:** SMB 2/3 access, integrated Media3 and libVLC playback engines, subtitles, playback resumption, watch history, and on-device credential encryption.
- **Design rationale:** Separate network access, playback control, and local data management to address varied media formats and usage conditions—not just play a sample video.

`Kotlin` · `Jetpack Compose` · `Media3 / libVLC` · `SMB`

### [Palworld Breeding Route Planner](https://github.com/ferretgeek/palworld-breeding-atlas)

Plan breeding routes from the Pals a player actually owns, comparing the steps and additional resources required by different options.

- **Implementation:** Multi-strategy route solving with inventory and parent-gender constraints; read-only save parsing with input and decompression limits; independently runnable solver regression tests.
- **Design rationale:** Move beyond static recipe lookup to constrained planning, while addressing data provenance, malformed inputs, and algorithm verification.

`Python` · `JavaScript` · `Route solving` · `Data parsing`

## Engineering practices

Practices I work to make concrete across my projects:

- **Design for failure:** Use health checks, transactions, persisted job progress, and backup / recovery workflows—not just happy-path validation.
- **Define data and permission boundaries:** Apply credential encryption, log redaction, read-only access, and write confirmation where appropriate, keeping data flows and permissions explainable.
- **Make delivery verifiable:** Use type checks, unit / regression tests, and CI across different projects, supported by environment requirements, deployment steps, and recovery documentation.

My main implementation areas are **Python services, TypeScript / React interfaces, Rust / Tauri desktop applications, and Kotlin Android development**, with SQLite, PostgreSQL, Docker, and systemd chosen according to storage and deployment needs.

## More projects

<details>
<summary><b>Explore 12 more projects · AI workflows / Mail services / Network and operations</b></summary>

### AI workflows and integrations

| Project | Focus and implementation |
| :--- | :--- |
| [Obsidian AI Writer](https://github.com/ferretgeek/obsidian-ai-writer) | User-selected note context, multiple model protocols, and diff previews before confirmed file writes. An independent derivative of `grok-obsidian`; see the repository NOTICE for attribution. |
| [Codex Quota Widget](https://github.com/ferretgeek/codex-quota-widget) | Windows overlay showing remaining quota, reset times, and low-quota alerts. |
| [Codex Multi-Account Quota Overview](https://github.com/ferretgeek/codex-quota-overview) | Import existing login files, inspect account quotas together, and export results. |
| [CLIProxyAPI Credential Check](https://github.com/ferretgeek/cliproxyapi-credential-check) | Inspect enabled accounts with optional availability and quota probes; distinguish an inventory from a live check. |

### Mail services and authorized access

| Project | Focus and implementation |
| :--- | :--- |
| [Domain Mail Inbox](https://github.com/ferretgeek/domain-mail-inbox) | SMTP receiving, an HTTP API, and SQLite storage using the Python standard library, with domain-scoped access and health checks. Receive-only; no outbound mail. |
| [Outlook Batch Inbox](https://github.com/ferretgeek/outlook-batch-inbox) | Query recent messages and verification codes across authorized mailboxes. |
| [IMAP Pickup Links](https://github.com/ferretgeek/imap-pickup-links) | Revocable web links that provide a controlled entry point to an existing mailbox. |
| [iCloud Code Finder](https://github.com/ferretgeek/icloud-code-finder) | Extract verification codes from recent messages in an authorized mailbox. |
| [Hide My Email Manager](https://github.com/ferretgeek/hide-my-email-manager) | Tags, notes, search, and backups for imported addresses; does not modify their state at Apple. |
| [Email Alias Generator](https://github.com/ferretgeek/email-alias-generator) | Generate tagged addresses locally in the browser; delivery support depends on the mailbox provider. |

### Network monitoring and operations

| Project | Focus and implementation |
| :--- | :--- |
| [Proxy Uptime Monitor](https://github.com/ferretgeek/proxy-uptime-monitor) | Access target pages through proxy nodes and record connectivity and failures over time. |
| [Palworld Server Panel](https://github.com/ferretgeek/palworld-server-panel) | Manage an existing Linux dedicated server: status, configuration, backups, and updates. |

</details>

---

**Want to try a project?** Open its repository for instructions and screenshots, and check **Releases** for published versions. Some projects require building from source or self-hosting.

**Want to discuss implementation or report an issue?** Use the relevant repository's **Issues**. Source code, architecture notes, and tests provide further context for each project.
