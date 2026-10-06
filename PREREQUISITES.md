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
| 5 | Jenkins | Run the CI/CD pipeline locally (via Docker) |
| 6 | Python 3.10+ | Run the sample app locally if needed |

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

## 5. Jenkins

Jenkins runs inside Docker, so Docker Desktop must be installed and running
first (step 2 above).

**macOS / Windows (both, via Docker)**
```bash
docker pull jenkins/jenkins:lts
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

**Verify (both)** — open [http://localhost:8080](http://localhost:8080) in a
browser; you should see the Jenkins unlock screen.

Stop it once you've confirmed it loads — we'll configure it properly in
Lab 2:
```bash
docker stop jenkins
```

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
docker ps -a --filter name=jenkins
python3 --version
```

Stuck on any of these? Reach out before the workshop — see the main
[README](README.md) for contact details.
