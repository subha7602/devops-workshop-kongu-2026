# Lab 2 — Local AI Agent for Kubernetes & Docker

Goal: build a local AI agent using LangChain + Ollama that can inspect the
Kind cluster and Docker containers from Lab 1, and answer questions about
their health.

## Prerequisites

- Lab 1 completed (Kind cluster running with `sample-webapp` deployed)
- [Ollama](https://ollama.com/download) installed
- Python 3.10+

## 1. Pull a local model

```bash
ollama pull llama3.2:1b
ollama serve   # if it isn't already running in the background
```

`llama3.2:1b` (~1.3GB) runs fine on 4GB-RAM laptops. If your machine has more
RAM, a bigger model reasons noticeably better:

| Laptop RAM | Model | Pull command |
|---|---|---|
| 4 GB | `llama3.2:1b` (default) | `ollama pull llama3.2:1b` |
| 8 GB | `llama3.2:3b` | `ollama pull llama3.2:3b` |
| 16 GB+ | `llama3.1` (8b) | `ollama pull llama3.1` |

If you pull a different model, update `MODEL_NAME` in `agent.py` to match.

## 2. Set up a virtual environment

```bash
cd hands-on/02-ai-agent
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Run the agent

```bash
python agent.py
```

Try asking:

- "List all pods in the cluster"
- "Are any pods unhealthy right now?"
- "What containers are currently running in Docker?"
- "Describe the sample-webapp pod"

## 4. See it catch a real issue

Go back to Lab 1, step 6, and break the deployment again:

```bash
kubectl set image deployment/sample-webapp sample-webapp=sample-webapp:doesnotexist
```

Then ask the agent: *"Are any pods unhealthy right now, and why?"*

## How it works

- `tools/k8s_tools.py` — wraps `kubectl` commands (`get pods`, `describe pod`, ...)
  as LangChain tools the agent can call.
- `tools/docker_tools.py` — wraps Docker CLI commands the same way.
- `agent.py` — wires a local Ollama model + these tools into a
  [LangGraph ReAct agent](https://langchain-ai.github.io/langgraph/), which
  decides which tool to call based on your question.

This is a proof-of-concept run entirely on your laptop — no cloud deployment,
no external API calls. The LLM only sees what the tools return.
