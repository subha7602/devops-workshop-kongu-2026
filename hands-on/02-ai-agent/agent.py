"""Local AI DevOps agent: a Kubernetes + Docker troubleshooting assistant.

Run with: python agent.py
Requires Ollama running locally with a model pulled, e.g.:
    ollama pull llama3.2:1b
"""

from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

from tools.docker_tools import container_logs, inspect_container, list_containers
from tools.k8s_tools import describe_pod, find_unhealthy_pods, list_pods

# llama3.2:1b fits 4GB-RAM laptops; swap to llama3.1 (8b) on 8GB+ RAM for better reasoning.
MODEL_NAME = "llama3.2:1b"

SYSTEM_PROMPT = """You are a local DevOps assistant. You can inspect a Kubernetes
cluster and Docker containers using the tools available to you. Always use a tool
to check real state before answering questions about pods or containers - never
guess. Summarize findings clearly and suggest a likely root cause when something
looks unhealthy."""


def build_agent():
    llm = ChatOllama(model=MODEL_NAME, temperature=0)
    tools = [
        list_pods,
        describe_pod,
        find_unhealthy_pods,
        list_containers,
        inspect_container,
        container_logs,
    ]
    return create_react_agent(llm, tools, state_modifier=SYSTEM_PROMPT)


def main():
    agent = build_agent()
    print("Local DevOps Agent ready. Ask about your cluster or containers.")
    print("Try: 'Are any pods unhealthy right now?'")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("you> ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue

        result = agent.invoke({"messages": [("user", question)]})
        answer = result["messages"][-1].content
        print(f"\nagent> {answer}\n")


if __name__ == "__main__":
    main()
