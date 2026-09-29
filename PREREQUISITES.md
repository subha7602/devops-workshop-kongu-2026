# Prerequisites — Install Before the Workshop

Install all of these **before** 10 October 2026. We won't have time to debug
installs during the session. After installing, run the "verify" command for
each tool and make sure it prints a version (not an error).

| # | Tool | Why |
|---|------|-----|
| 1 | Git | Clone and manage the workshop repo |
| 2 | Docker Desktop | Build and run containers |
| 3 | kubectl | Talk to a Kubernetes cluster |
| 4 | kind | Run a Kubernetes cluster locally, inside Docker |
| 5 | Ollama | Run the LLM locally for the AI agent |
| 6 | Python 3.10+ | Run the agent code |

---

## 1. Git

**macOS**
```bash
brew install git
```
No Homebrew? Install it first: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

**Windows** (PowerShell)
```powershell
winget install --id Git.Git -e --source winget
```

**Verify (both)**
```bash
git --version
```

---

## 2. Docker Desktop

**macOS**
```bash
brew install --cask docker
```
Then open **Docker.app** from Applications once — Docker Desktop needs to be
running in the background before you use `docker` or `kind`.

**Windows** (PowerShell, run as Administrator)
```powershell
winget install -e --id Docker.DockerDesktop
```
Docker Desktop on Windows requires **WSL2**. If it's not already enabled:
```powershell
wsl --install
```
Restart your machine, then launch Docker Desktop once from the Start menu.

**Verify (both)**
```bash
docker --version
docker run hello-world
```

---

## 3. kubectl

**macOS**
```bash
brew install kubectl
```

**Windows** (PowerShell)
```powershell
winget install -e --id Kubernetes.kubectl
```

**Verify (both)**
```bash
kubectl version --client
```

---

## 4. kind (Kubernetes in Docker)

Docker Desktop must be installed and running first.

**macOS**
```bash
brew install kind
```

**Windows** (PowerShell)
```powershell
choco install kind
```
No Chocolatey? Install it first from [chocolatey.org/install](https://chocolatey.org/install), or install kind manually:
```powershell
curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.23.0/kind-windows-amd64
Move-Item .\kind-windows-amd64.exe C:\Windows\System32\kind.exe
```

**Verify (both)**
```bash
kind --version
```

---

## 5. Ollama

**macOS**
```bash
brew install ollama
```
Or download the installer from [ollama.com/download](https://ollama.com/download).

**Windows** (PowerShell)
```powershell
winget install -e --id Ollama.Ollama
```
Or download the installer from [ollama.com/download](https://ollama.com/download).

**Verify (both)**
```bash
ollama --version
```

**Pull the model we'll use** (do this before the workshop, not on workshop Wi-Fi):
```bash
ollama pull llama3.2:1b
```

`llama3.2:1b` (~1.3GB) is sized to run on 4GB-RAM laptops. If your laptop has
more RAM, a bigger model answers noticeably better:

| Laptop RAM | Model | Pull command |
|---|---|---|
| 4 GB | `llama3.2:1b` (default) | `ollama pull llama3.2:1b` |
| 8 GB | `llama3.2:3b` | `ollama pull llama3.2:3b` |
| 16 GB+ | `llama3.1` (8b) | `ollama pull llama3.1` |

---

## 6. Python 3.10+

**macOS**
```bash
brew install python@3.11
```

**Windows** (PowerShell)
```powershell
winget install -e --id Python.Python.3.11
```

**Verify (both)**
```bash
python3 --version   # macOS
python --version    # Windows
```

---

## All-in-one verify checklist

Run these after installing everything. Every line should print a version, not
an error:

```bash
git --version
docker --version
kubectl version --client
kind --version
ollama --version
python3 --version
```

Stuck on any of these? Reach out before the workshop — see the main
[README](README.md) for contact details.
