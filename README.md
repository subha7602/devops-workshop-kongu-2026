# DevOps Workshop — Kongu 2026

**Built a Local AI Agent for Kubernetes & Docker using LangChain + Ollama**

A hands-on workshop on building a local, AI-powered DevOps agent that can
inspect Kubernetes clusters and Docker containers — no cloud dependency, runs
entirely on your laptop.

- **Date:** 10 October 2026
- **Time:** 9:30 AM – 4:00 PM
- **Presenter:** Subhashini S V ([LinkedIn](https://linkedin.com/in/subhashini-sv))


## Before you arrive

Please do this **before the workshop** — we won't have time to debug installs
during the session:

1. Read `Git-GitHub-101.pdf` (shared separately) and make sure you can clone
   this repo.
2. Install everything in [PREREQUISITES.md](PREREQUISITES.md) (Git, Docker
   Desktop, kubectl, kind, Ollama, Python) — it has copy-paste commands for
   both macOS and Windows.
3. Clone this repo:
   ```bash
   git clone <this-repo-url>
   cd devops-workshop-kongu-2026
   ```
4. Pull the model we'll use, so you're not doing it on workshop Wi-Fi:
   ```bash
   ollama pull llama3.2:1b
   ```
   This is a small model (~1.3GB) chosen to fit 4GB-RAM laptops. On 8GB+ RAM,
   see [Lab 2](hands-on/02-ai-agent/) for bigger, better-reasoning options.

## What we'll build

1. **[Lab 1](hands-on/01-sample-webapp/)** — a sample web app, containerized
   with Docker and deployed to a local Kubernetes cluster (Kind).
2. **[Lab 2](hands-on/02-ai-agent/)** — a local AI agent (LangChain + Ollama)
   that can list pods, describe pod issues, and inspect Docker containers on
   request.

## Agenda (9:30 AM – 4:00 PM)

| Time | Session |
|---|---|
| 9:30 – 9:45 | Welcome & workshop overview |
| 9:45 – 10:15 | Theory: DevOps + local AI agents, why run LLMs locally |
| 10:15 – 10:45 | Theory: Docker & Kubernetes fundamentals recap |
| 10:45 – 11:00 | Break |
| 11:00 – 11:30 | Theory: LangChain + Ollama architecture, how agent tools work |
| 11:30 – 12:30 | Hands-on: Lab 1 — Docker build + Kind cluster + deploy |
| 12:30 – 1:00 | Lunch |
| 1:00 – 1:15 | **Quiz** |
| 1:15 – 2:15 | Hands-on: Lab 2 — build the LangChain + Ollama agent |
| 2:15 – 3:15 | Hands-on: connect agent tools, break things, watch it diagnose |
| 3:15 – 3:45 | Demo showcase + Q&A |
| 3:45 – 4:00 | Wrap-up & resources |

## Repo structure

```
hands-on/
  01-sample-webapp/   # Flask app + Dockerfile + k8s manifests
  02-ai-agent/         # LangChain + Ollama agent with kubectl/docker tools
```
