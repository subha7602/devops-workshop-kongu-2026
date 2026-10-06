# DevOps Workshop — Kongu 2026

**Git → Docker → Kubernetes → Jenkins: a hands-on DevOps pipeline, built end to end on your laptop**

A hands-on workshop covering core DevOps tooling — version control with Git,
containerization with Docker, orchestration with Kubernetes, and continuous
integration with Jenkins — ending with a real pipeline: push code to Git and
watch it roll out automatically to a local Kubernetes cluster.

- **Date:** 10 October 2026
- **Time:** 9:30 AM – 4:00 PM
- **Presenter:** Subhashini S V ([LinkedIn](https://linkedin.com/in/subhashini-sv))


## Before you arrive

Please do this **before the workshop** — we won't have time to debug installs
during the session:

1. Read `Git-GitHub-101.pdf` (shared separately) and make sure you can clone
   this repo.
2. Install everything in [PREREQUISITES.md](PREREQUISITES.md) (Git, Docker
   Desktop, kubectl, kind, Jenkins, Python) — it has copy-paste commands for
   both macOS and Windows.
3. Clone this repo:
   ```bash
   git clone <this-repo-url>
   cd devops-workshop-kongu-2026
   ```

## What we'll build

1. **[Lab 1](hands-on/01-sample-webapp/)** — a sample web app, containerized
   with Docker and deployed to a local Kubernetes cluster (Kind).
2. **[Lab 2](hands-on/02-jenkins-cicd/)** — a Jenkins pipeline that builds
   that app and deploys it on every Git push, so changes show up locally
   automatically — the full Git → Jenkins → Kubernetes loop.

## Agenda (9:30 AM – 4:00 PM)

| Time | Session |
|---|---|
| 9:30 – 9:45 | Welcome & workshop overview |
| 9:45 – 10:15 | Theory: DevOps intro, architecture & lifecycle |
| 10:15 – 10:45 | Theory: Version control with Git & GitHub |
| 10:45 – 11:00 | Break |
| 11:00 – 11:30 | Theory: Docker & Kubernetes fundamentals |
| 11:30 – 12:30 | Hands-on: Lab 1 — Docker build + Kind cluster + deploy |
| 12:30 – 1:00 | Lunch |
| 1:00 – 1:15 | **Quiz** |
| 1:15 – 1:45 | Theory: Continuous Integration with Jenkins + JIRA-driven development |
| 1:45 – 3:15 | Hands-on: Lab 2 — Git push → Jenkins pipeline → local Kubernetes rollout |
| 3:15 – 3:45 | Demo showcase + Q&A |
| 3:45 – 4:00 | Wrap-up & resources |

## Repo structure

```
hands-on/
  01-sample-webapp/   # Flask app + Dockerfile + k8s manifests
  02-jenkins-cicd/     # Jenkinsfile: Git push -> build -> deploy to Kind
```
